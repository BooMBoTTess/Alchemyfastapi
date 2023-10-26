from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_async_session
from database.models import User, staff
from src.Informations.schemas import staff_schema

router = APIRouter(
    prefix='/info',
    tags=['database']
)

# https://habr.com/ru/articles/513328/
@router.get('/',
            response_model=list[staff_schema],
            )  # ЭТА ХУЙНЯ НУЖНА ЧТОБЫ ОН ПОНЯЛ КАК ОТПРАВИТЬ
async def get_staff(dep: int = 1,
                              session: AsyncSession = Depends(get_async_session)):  # ТУТ НУЖНО ВЗЯТЬ НАШУ ЕБУЧУЮ СЕССИЮ
    query = select(staff)  # НАШ ЗАПРОС
    result = await session.execute(query)  # ДОЛЖНО БЫТЬ С АВАЙТОМ ПОТОМУ ЧТО У НАС АСИНХРОННОЕ ГОВНО
    # print(result.all())

    return result.all()  # ВЕРНЕТ ВСЕ СТРОКИ, БЕЗ ВЕРХНЕЙ ХУЙНИ ВЫДАСТ ОШИБКУ

@router.post('/', status_code=status.HTTP_201_CREATED)
def add_staff(staff_person : staff_schema , session: AsyncSession = Depends(get_async_session)):
    st = staff(
        full_name=staff_person.full_name,
        department=staff_person.department,
        post=staff_person.post,
    )
    session.add(st)
    return 22