from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, ConfigDict


class ScheduleCreate(BaseModel):
    user_id: int = Field(gt=0, description="ID пользователя")
    drug_name: str = Field(max_length=256, description="Название препарата")
    rec_frequency: int = Field(gt=0, description="Частота приема в часах")
    duration: Optional[int] = Field(
        default=None,
        gt=0,
        description="Длительность приёма лекарств в днях (не указывать при постоянном приёме)"
    )
    model_config = ConfigDict(from_attributes=True)

class ScheduleCreateResponse(BaseModel):
    schedule_id: int = Field(gt=0, description="ID расписания")
    model_config = ConfigDict(from_attributes=True)

class SchedulesIdsResponse(BaseModel):
    schedules_ids: List[int] = Field(description="Список ID расписаний")
    model_config = ConfigDict(from_attributes=True)


class ScheduleInfoResponse(BaseModel):
    drug_name: str = Field(description="Название препарата")
    created_at: datetime = Field(description="Дата и время создания расписания")
    rec_frequency: int = Field(description="Частота приема в часах")
    duration: Optional[int] = Field(
        default=None,
        description="Длительность приёма лекарств в днях (не указывать при постоянном приёме)"
    )
    medication_times: List[datetime] = Field(description="Время приёма лекарств")
    model_config = ConfigDict(from_attributes=True)


class NextTakingsResponse(BaseModel):
    drug_name: str = Field(description="Название препарата")
    medication_times: List[datetime] = Field(description="Время приёма лекарств")
    model_config = ConfigDict(from_attributes=True)
