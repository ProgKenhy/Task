from datetime import datetime
from typing import List
from config.models import created_at

from pydantic import BaseModel, Field, ConfigDict


class ScheduleCreate(BaseModel):
    user_id: int = Field(gt=0, description="ID пользователя")
    drug_name: str = Field(max_length=256, description="Название препарата")
    rec_frequency: int = Field(gt=0, description="Частота приема")
    duration: int | None = Field(default=None, gt=0,
                                 description="Длительность приёма лекарств в днях (не указывать при постоянном приёме)")


class SchedulesIdsResponse(BaseModel):
    schedules_ids: list[int]
    model_config = ConfigDict(from_attributes=True)


class ScheduleInfoResponse(BaseModel):
    drug_name: str
    created_at: created_at
    rec_frequency: int
    duration: int | None
    medication_times: List[datetime]

class NextTakingsResponse(BaseModel):
    drug_name: str
    medication_times: List[datetime]