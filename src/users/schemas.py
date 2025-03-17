from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    pass


class UsersSelect(BaseModel):
    user_id: int
    model_config = ConfigDict(from_attributes=True)
