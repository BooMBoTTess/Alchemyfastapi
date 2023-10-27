from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
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
async def get_all_staff(session: AsyncSession = Depends(get_async_session)):

    query = select(department)
    result = await session.execute(query)
    departments = result.scalars().all()

    query = select(post)
    result = await session.execute(query)
    posts = result.scalars().all()
    dep_post = [{dep_elem.id: dep_elem.name for dep_elem in departments},
                {post_elem.id: post_elem.name for post_elem in posts}]

    return dep_post
@router.get('/{department_path}/{post_path}',
            response_model=list[staff_schema]
            )
async def get_staff(department_path: int, post_path: int = None,
                              session: AsyncSession = Depends(get_async_session)):  # ТУТ НУЖНО ВЗЯТЬ НАШУ ЕБУЧУЮ СЕССИЮ

    query = select(staff)
    result = await session.execute(query)
    staff_elem = result.scalars().all()
    responce = [staff_elem[i] for i in range(len(staff_elem))]
    print(responce)

    return responce  


# https://habr.com/ru/articles/513328/
@router.get('/test'
            #response_model=list[staff_schema],
            )  # ЭТА ХУЙНЯ НУЖНА ЧТОБЫ ОН ПОНЯЛ КАК ОТПРАВИТЬ
async def get_staff_test(department_path: int, post_path: int,
                              session: AsyncSession = Depends(get_async_session)):  # ТУТ НУЖНО ВЗЯТЬ НАШУ ЕБУЧУЮ СЕССИЮ
    query = select(staff)  # НАШ ЗАПРОС
    print(query)
    result = await session.execute(query)# ДОЛЖНО БЫТЬ С АВАЙТОМ ПОТОМУ ЧТО У НАС АСИНХРОННОЕ ГОВНО
    rows = result.scalars().all()
    print(1, rows)
    result = await session.execute(query)

    for s in result.scalars():
        print(2, s.id, s.full_name, s.department, type(s))

    result = await session.execute(query)
    print(3, result.all())

    return 11  # ВЕРНЕТ ВСЕ СТРОКИ, БЕЗ ВЕРХНЕЙ ХУЙНИ ВЫДАСТ ОШИБКУ


@router.post('/', status_code=status.HTTP_201_CREATED)
def add_staff(staff_person : staff_schema , session: AsyncSession = Depends(get_async_session)):
    st = staff(
        full_name=staff_person.full_name,
        fk_department_id=staff_person.department,
        fk_post_id=staff_person.post,
    )
    print(st)
    session.add(st)
    return 202
