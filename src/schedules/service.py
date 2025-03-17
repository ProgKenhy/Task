from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from schedules.models import ScheduleOrm
from schedules.schemas import ScheduleCreate


class ScheduleDal:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_schedule(self, body: ScheduleCreate) -> ScheduleOrm:
        schedule = ScheduleOrm(**body.model_dump())
        self.db_session.add(schedule)
        await self.db_session.commit()
        await self.db_session.refresh(schedule)
        return schedule


    async def select_schedules_ids(self, user_id: int) -> list[int]:
        query = select(ScheduleOrm).where(ScheduleOrm.user_id == user_id)
        result = await self.db_session.execute(query)
        schedules = result.scalars().all()
        schedules_ids = [schedule.schedule_id for schedule in schedules]
        return schedules_ids

    async def select_schedule(self, user_id: int, schedule_id: int) -> ScheduleOrm:
        query = select(ScheduleOrm).where(ScheduleOrm.user_id == user_id, ScheduleOrm.schedule_id == schedule_id)
        result = await self.db_session.execute(query)
        schedule = result.scalars().first()
        return schedule
