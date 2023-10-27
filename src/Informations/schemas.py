from typing import Optional
from pydantic import BaseModel


class staff_schema(BaseModel):
    full_name: str
    department: int
    post: int
