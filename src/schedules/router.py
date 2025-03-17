from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from schedules.schemas import ScheduleCreate, SchedulesIdsResponse, ScheduleInfoResponse
from schedules.service import ScheduleDal
from config.dependencies import get_db_session

schedule_router = APIRouter()
schedules_router = APIRouter()


@schedule_router.post('', response_model=ScheduleCreate)
async def create_schedule(body: ScheduleCreate, db_session: AsyncSession = Depends(get_db_session)):
    schedule_dal = ScheduleDal(db_session)
    new_schedule = await schedule_dal.create_schedule(body)
    return ScheduleCreate.model_validate(new_schedule, from_attributes=True)


@schedule_router.get('', response_model=ScheduleInfoResponse)
async def select_schedule(user_id:int, schedule_id: int, db_session: AsyncSession = Depends(get_db_session)):
    schedule_dal = ScheduleDal(db_session)
    schedule = await schedule_dal.select_schedule(user_id=user_id, schedule_id=schedule_id)
    return schedule


@schedules_router.get('', response_model=SchedulesIdsResponse)
async def select_schedules_ids(user_id: int = Query(..., gt=0), db_session: AsyncSession = Depends(get_db_session)):
    schedule_dal = ScheduleDal(db_session)
    schedules_ids = await schedule_dal.select_schedules_ids(user_id)
    return SchedulesIdsResponse(schedules_ids=schedules_ids)


