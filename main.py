from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI

from models import UserClass, Gender, Role

app = FastAPI()

db: List[UserClass] = [
    UserClass(
        id=uuid4(),
        first_name='bonas',
        last_name='king',
        middle_name='you',
        gender=Gender.male,
        roles=[Role.user]
    ),
    UserClass(
        id=uuid4(),
        first_name='Alex',
        last_name='Jones',
        middle_name='you',
        gender=Gender.male,
        roles=[Role.user]
    )
]


@app.get("/")
async def root():
    return {"hello": "world"}


@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/user")
async def register_user(user: UserClass):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/user/{id}")
async def delete_user(id: UUID):
    if UserClass.id == id :
        db.remove(UserClass)
        return


