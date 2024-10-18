from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/')
async def power_str(request: Request) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "users": users})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


@app.get('/users/{user_id}')
async def dict_get(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id-1]})


@app.post('/users/{username}/{age}')
async def create_user(user: User, username: str, age: int) -> User:
    user.username, user.id, user.age = username, len(users) + 1, age
    users.append(user)
    return user


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