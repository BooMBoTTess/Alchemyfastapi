from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, TIMESTAMP, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from database.models import department


