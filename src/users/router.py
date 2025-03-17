from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from users.schemas import UserCreate, UsersSelect
from users.service import UserDal
from config.dependencies import get_db_session

users_router = APIRouter()


@users_router.post('/create_user', response_model=UserCreate)
async def create_user(db_session: AsyncSession = Depends(get_db_session)):
    user_dal = UserDal(db_session)
    new_user = await user_dal.create_user()
    return new_user

@users_router.get('/select_users', response_model=list[UsersSelect])
async def select_users(db_session: AsyncSession = Depends(get_db_session)):
    user_dal = UserDal(db_session)
    return await user_dal.select_users()
