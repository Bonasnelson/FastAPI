from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum

from pydantic import BaseModel


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    admin = "admin"
    user = "user"


class UserClass(BaseModel):
    id: Optional[UUID] = uuid4
    first_name: str
    last_name: str
    middel_name: Optional[str]
    gender = Gender
    role = List[Role]
