from fastapi import APIRouter

rout = APIRouter(prefix='/user', tags=['user'])


@rout.get('/')
async def all_users():
    pass


@rout.get('/user_id')
async def user_by_id():
    pass


@rout.post('/create')
async def create_user():
    pass


@rout.put('/update')
async def update_user():
    pass


@rout.delete('/delete')
async def delete_user():
    pass
