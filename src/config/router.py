from fastapi import APIRouter
from schedules.router import schedule_router, schedules_router, next_takings_router

api_router = APIRouter()

api_router.include_router(schedule_router, prefix='/schedule', tags=["schedules"])
api_router.include_router(schedules_router, prefix='/schedules', tags=["schedules"])
api_router.include_router(next_takings_router, prefix='/next-takings', tags=["schedules"])