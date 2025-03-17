from pydantic import BaseModel, Field, ConfigDict

class ScheduleCreate(BaseModel):
    user_id: int = Field(gt=0, description="ID пользователя должен быть положительным числом")
    drug_name: str = Field(max_length=256, description="Название препарата не должно превышать 256 символов")
    rec_frequency: int = Field(gt=0, description="Частота приема должна быть положительным числом")
    duration: int = Field(gt=0, description="Длительность должна быть положительным числом")

class SchedulesSelect(BaseModel):
    user_id: int = Field(gt=0)

class SchedulesIdsResponse(BaseModel):
    schedules_ids: list[int]
    model_config = ConfigDict(from_attributes=True)

class ScheduleInfoResponse(BaseModel):
    drug_name: str
    rec_frequency: int
    duration: int
