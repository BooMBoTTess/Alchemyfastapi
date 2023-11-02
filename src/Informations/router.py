from fastapi import APIRouter, Depends, status, Request
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse, HTMLResponse

from database.database import get_async_session
from database.models import staff, department, post
from src.Informations.schemas import staff_schema
from fastapi.templating import Jinja2Templates
from config import PATH_TO_TEMPLATES

router = APIRouter(
    prefix='/info',
    tags=['database']
)


templates = Jinja2Templates(directory=PATH_TO_TEMPLATES)


@router.get('/')
async def get_dep_post(request: Request, session: AsyncSession = Depends(get_async_session)):
    query = select(department)
    result = await session.execute(query)
    departments = result.scalars().all()

    response = templates.TemplateResponse('information.html', status_code=202,
                                      context= {'request': request, 'data': [departments]})
    return response


@router.get('/{department_path}')
async def get_staff(department_path: int, request: Request,
                    session: AsyncSession = Depends(get_async_session)):
    query = ((select(staff.full_name, department.name, post.name, department.id)
              .join(department).filter(staff.fk_department_id == department.id)
              .join(post).filter(staff.fk_post_id == post.id))
             .order_by(department.id).order_by(post.id))
    result = await session.execute(query)
    json_staff = []
    result = result.all()
    for r in result:
        if result[4] == department_path:
            json_staff.append([r[0], r[1], r[2]])

    if json_staff == []:
        return templates.TemplateResponse('information_by_dep.html',
                                          context={'request': request,
                                                   'data': json_staff,
                                                   'department': 'Отсуствует'
                                                   },
                                          status_code=204)
    else:
        return templates.TemplateResponse('information_by_dep.html',
                                          context={'request': request,
                                                   'data': json_staff,
                                                   'department': json_staff[0][1]
                                                   },
                                          status_code=200)



# https://habr.com/ru/articles/513328/
@router.get('/tests'
            # response_model=list[staff_schema],
            )  # ЭТА ХУЙНЯ НУЖНА ЧТОБЫ ОН ПОНЯЛ КАК ОТПРАВИТЬ
async def get_staff_test(department_path: int, post_path: int,
                         session: AsyncSession = Depends(get_async_session)):  # ТУТ НУЖНО ВЗЯТЬ НАШУ ЕБУЧУЮ СЕССИЮ
    query = select(staff)  # НАШ ЗАПРОС
    print(query)
    result = await session.execute(query)  # ДОЛЖНО БЫТЬ С АВАЙТОМ ПОТОМУ ЧТО У НАС АСИНХРОННОЕ ГОВНО
    rows = result.scalars().all()
    print(1, rows)
    result = await session.execute(query)

    for s in result.scalars():
        print(2, s.id, s.full_name, s.department, type(s))

    result = await session.execute(query)
    print(3, result.all())

    return 11  # ВЕРНЕТ ВСЕ СТРОКИ, БЕЗ ВЕРХНЕЙ ХУЙНИ ВЫДАСТ ОШИБКУ


@router.post('/')
def add_staff(staff_person: staff_schema, request: Request, session: AsyncSession = Depends(get_async_session)):
    st = staff(
        full_name=staff_person.full_name,
        fk_department_id=staff_person.department,
        fk_post_id=staff_person.post,
    )
    print(request)

    session.add(st)
    return 202
