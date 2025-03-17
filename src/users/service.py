from sqlalchemy import select
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from users.models import UsersOrm
from users.schemas import UsersSelect

class UserDal:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self) -> UsersOrm:
        user = UsersOrm()
        self.db_session.add(user)
        await self.db_session.commit()
        await self.db_session.refresh(user)
        return user


    async def select_users(self) -> List[UsersSelect]:
        query = select(UsersOrm)
        result = await self.db_session.execute(query)
        users = result.scalars().all()
        return [UsersSelect.model_validate(user, from_attributes=True) for user in users]
