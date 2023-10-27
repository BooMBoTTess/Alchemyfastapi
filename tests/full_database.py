from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from database.models import post, department, staff

DATABASE_URL = "postgresql://myuser:1234@localhost/site_database"

engine = create_engine(DATABASE_URL, echo=True)
session = Session(engine)


def full_by_hands(post_table, dep_table, staff_table):
    try:
        session.add_all(post_table)
        session.commit()
        session.add_all(dep_table)
        session.commit()
        session.add_all(staff_table)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()


if __name__ == '__main__':
    fake = Faker('ru_RU')

    post_table = [post(id=0, name='Глава начальника'),
                  post(id=1,name='Начальник'),
                  post(id=2,name='Почти начальник'),
                  post(id=3,name='Чальник')
                  ]
    dep_table = [department(id=0, name='Отдел ведения анимешных девочек'),
                 department(id=1, name='Отдел ведения анимешных мальчиков'),
                 department(id=2, name='Отдел мемасиков'),
                 ]

    staff_table = [staff(id=0,
                         full_name='Малый Артём Владиславович',
                         fk_department_id=0,
                         fk_post_id=0),
                   staff(
                       id=1,
                       full_name='Светлый Данил Олегович',
                       fk_department_id=0,
                       fk_post_id=1,
                   ),
                   staff(
                       id=2,
                       full_name='Быстрая Елена Григорьевна',
                       fk_department_id=1,
                       fk_post_id=0,
                   )
                   ]
    counter = 3
    for d in range(len(dep_table)):
        for p in range(len(post_table)):
            staff_table.append(staff(id=counter, full_name=fake.name(), fk_department_id=d, fk_post_id=p))
            counter += 1

    full_by_hands(post_table, dep_table, staff_table)
