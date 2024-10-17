from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def dict_get() -> list:
    return users


@app.post('/users/{username}/{age}')
async def create_user(user: User, username: str, age: int) -> User:
    user.username, user.id, user.age = username, len(users) + 1, age
    users.append(user)
    return users[user.id - 1]


@app.put('/users/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str,age: int) -> User:
    try:
        user = users[user_id - 1]
        user.username = username
        user.age = age
        return users[user_id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/users/{user_id}')
async def delete_user(user_id: int) -> User:
    try:
        user = list(filter(lambda x: x.id == user_id, users))[0]
        users.remove(user)
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
