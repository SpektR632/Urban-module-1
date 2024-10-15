from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def dict_get() -> dict:
    return users


@app.post('/users/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                      age: Annotated[int, Path(eq=18, el=120, description='Enter age', example="24")]) -> str:
    current_user = str(int(max(users, key=int)) + 1)
    users[current_user] = f'Имя: {username}, Возраст: {age}'
    return f'User {current_user} is registered'


@app.put('/users/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[str, Path(eq=1, el=100, description='Enter User ID', example='1')],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                      age: Annotated[int, Path(eq=18, el=120, description='Enter age', example="24")]) -> str:
    users[user_id] = f'Имя: {username}, Возраст: {age}'
    return f'User {user_id} has been updated'


@app.delete('/users/{user_id}')
async def delete_user(user_id: Annotated[str, Path(eq=1, el=100, description='Enter User ID', example='1')]) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"
