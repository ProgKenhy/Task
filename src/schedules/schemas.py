from fastapi import HTTPException
from pydantic import BaseModel, Field, ConfigDict, model_validator


class ScheduleCreate(BaseModel):
    user_id: int = Field(gt=0, description="ID пользователя")
    drug_name: str = Field(max_length=256, description="Название препарата")
    rec_frequency: int = Field(gt=0, description="Частота приема")
    duration: int | None = Field(default=None, gt=0, description="Длительность приёма лекарств в днях (необязательно при постоянном приёме)")
    is_continuous: bool = Field(default=False, description="Является ли приём лекарств постоянным?")

    @model_validator(mode='after')
    def validate_duration(self):
        if not self.is_continuous and self.duration is None:
            raise HTTPException(
                status_code=400,
                detail="Duration must be specified for non-continuous medications"
            )
        return self

class SchedulesIdsResponse(BaseModel):
    schedules_ids: list[int]
    model_config = ConfigDict(from_attributes=True)

class ScheduleInfoResponse(BaseModel):
    drug_name: str
    rec_frequency: int
    duration: int | None
    is_continuous: bool
