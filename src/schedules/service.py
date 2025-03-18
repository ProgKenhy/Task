from datetime import datetime, time, timedelta, timezone
from typing import List

from fastapi import HTTPException
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
        if not schedules_ids:
            raise HTTPException(status_code=404, detail="No schedules found for this user")
        return schedules_ids

    async def select_schedule(self, user_id: int, schedule_id: int) -> ScheduleOrm:
        query = select(ScheduleOrm).where(ScheduleOrm.user_id == user_id, ScheduleOrm.schedule_id == schedule_id)
        result = await self.db_session.execute(query)
        schedule = result.scalars().first()
        if not schedule:
            raise HTTPException(status_code=404, detail="Schedule not found")
        return schedule


def generate_medication_times(schedule: ScheduleOrm, hours_ahead: int) -> List[datetime]:
    time_day_start = time(8, 0)  # TODO: Вынести в constants.py
    time_day_end = time(22, 0)
    current_time = datetime.now()
    medication_times = []
    print("time", current_time)

    end_window = current_time + timedelta(hours=hours_ahead)

    if schedule.duration is not None:
        treatment_end = schedule.created_at + timedelta(days=schedule.duration)
        end_window = min(end_window, treatment_end)

    if current_time.date() != schedule.created_at.date():
        rec_time = datetime.combine(current_time.date(), time_day_start)
    else:
        remainder = schedule.created_at.minute % 15
        if remainder > 0:
            rec_time = schedule.created_at + timedelta(minutes=15 - remainder)
        else:
            rec_time = schedule.created_at

    while rec_time <= end_window:
        if time_day_start <= rec_time.time() <= time_day_end:
            if rec_time >= current_time:
                medication_times.append(rec_time)
            rec_time += timedelta(hours=schedule.rec_frequency)
        else:
            next_day = rec_time.date() + timedelta(days=1)
            rec_time = datetime.combine(next_day, time_day_start)
            if rec_time > end_window:
                break
    return medication_times
