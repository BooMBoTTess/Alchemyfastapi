from fastapi import Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_async_session
from database.models import staff


def foo(session = Depends(get_async_session)):

    st = staff(
        full_name='Быстрая Елена Григорьевна',
        department='Отдел ведения анимешных кошкомальчиков',
        post='Заместитель главы отдела',
    )
    session.add(arr)

if __name__ == '__main__':
    arr = [staff(full_name = 'Малый Артём Владиславович',
               department='Отдел ведения анимешных кошкодевочек',
               post='Глава отдела'),
           staff(
               full_name='Светлый Данил Олегович',
               department='Отдел ведения анимешных кошкодевочек',
               post='Заместитель главы отдела',
           ),
           staff(
               full_name='Быстрая Елена Григорьевна',
               department='Отдел ведения анимешных кошкомальчиков',
               post='Заместитель главы отдела',
           )
           ]
    foo()