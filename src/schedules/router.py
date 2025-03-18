from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from schedules.schemas import ScheduleCreate, SchedulesIdsResponse, ScheduleInfoResponse, NextTakingsResponse
from schedules.service import ScheduleDal, generate_medication_times
from config.dependencies import get_db_session
from config.settings import settings

schedule_router = APIRouter() # 3 роутера только потому, что адреса в ТЗ странные (не под одним префиксом), хотя раздел один
schedules_router = APIRouter()
next_takings_router = APIRouter()


@schedule_router.post('', response_model=ScheduleCreate)
async def create_schedule(body: ScheduleCreate, db_session: AsyncSession = Depends(get_db_session)):
    schedule_dal = ScheduleDal(db_session)
    new_schedule = await schedule_dal.create_schedule(body)
    return ScheduleCreate.model_validate(new_schedule, from_attributes=True)


@schedules_router.get('', response_model=SchedulesIdsResponse)
async def select_schedules_ids(user_id: int = Query(..., gt=0), db_session: AsyncSession = Depends(get_db_session)):
    schedule_dal = ScheduleDal(db_session)
    schedules_ids = await schedule_dal.select_schedules_ids(user_id)
    return SchedulesIdsResponse(schedules_ids=schedules_ids)

@schedule_router.get('', response_model=ScheduleInfoResponse)
async def select_schedule(user_id:int, schedule_id: int, db_session: AsyncSession = Depends(get_db_session)):
    schedule_dal = ScheduleDal(db_session)
    schedule = await schedule_dal.select_schedule(user_id=user_id, schedule_id=schedule_id)
    hours_until_22 = (22 - datetime.now().hour) or 24
    medication_times = generate_medication_times(
        schedule=schedule,
        hours_ahead=hours_until_22
    )
    return ScheduleInfoResponse(
        drug_name=schedule.drug_name,
        created_at=schedule.created_at,
        rec_frequency=schedule.rec_frequency,
        duration=schedule.duration,
        medication_times=medication_times
    )


@next_takings_router.get('', response_model=List[NextTakingsResponse])
async def select_next_takings(user_id: int, db_session: AsyncSession = Depends(get_db_session)):
    schedule_dal = ScheduleDal(db_session)
    schedules_ids = await schedule_dal.select_schedules_ids(user_id)
    result = []
    for schedule_id in schedules_ids:
        schedule = await schedule_dal.select_schedule(user_id=user_id, schedule_id=schedule_id)
        medication_times = generate_medication_times(
            schedule=schedule,
            hours_ahead=settings.NEXT_TAKINGS_HOURS_AHEAD
        )
        if medication_times:
            result.append(
                NextTakingsResponse(
                    drug_name=schedule.drug_name,
                    medication_times=medication_times
                )
            )
    return result
