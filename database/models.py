from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, Column, Table, String, TIMESTAMP, ForeignKey, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class staff(Base):
    __tablename__ = 'staff'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String(length=100))
    department: Mapped[str] = mapped_column(String(length=50))
    post: Mapped[str] = mapped_column(String(length=50))

    def __repr__(self) -> str:
        return f"User(id={self.id!r},name={self.full_name!r})"

class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'User'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    registered_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)