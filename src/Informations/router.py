from fastapi import APIRouter, Depends, status, Request
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse, HTMLResponse

from database.database import get_async_session
from database.models import staff, department, post
from src.Informations.schemas import staff_schema

router = APIRouter(
    prefix='/info',
    tags=['database']
)


@router.get('/',
            # response_model=list[staff_schema]
            )
async def get_dep_post(session: AsyncSession = Depends(get_async_session)):
    query = select(department)
    result = await session.execute(query)
    departments = result.scalars().all()

    query = select(post)
    result = await session.execute(query)
    posts = result.scalars().all()
    dep_post = [{dep_elem.id: dep_elem.name for dep_elem in departments},
                {post_elem.id: post_elem.name for post_elem in posts}]

    return dep_post


@router.get('/{department_path}',
            # response_model=list[staff_schema]
            )
async def get_staff(department_path: int, request: Request,
                    session: AsyncSession = Depends(get_async_session)):  # ТУТ НУЖНО ВЗЯТЬ НАШУ ЕБУЧУЮ СЕССИЮ
    print('req', request.headers)
    query = ((select(staff.full_name, department.name, post.name)
              .join(department).filter(staff.fk_department_id == department.id)
              .join(post).filter(staff.fk_post_id == post.id))
             .where(department.id == department_path)
             .order_by(department.id).order_by(post.id))
    result = await session.execute(query)
    json_staff = []
    for r in result.all():
        json_staff.append({r[0]: [r[1], r[2]]})

    jsresponse = JSONResponse(content=json_staff)
    jsresponse.status_code = 202

    return jsresponse


# https://habr.com/ru/articles/513328/
@router.get('/test'
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

    response = HTMLResponse(status_code=202, content=)
    session.add(st)
    return response
