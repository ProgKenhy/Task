from typing import Optional

from sqlalchemy import String, Integer, Boolean
from sqlalchemy.testing.schema import mapped_column

from config.models import Base, str_256, intpk, created_at
from sqlalchemy.orm import Mapped




class ScheduleOrm(Base):
    __tablename__ = 'schedules'
    schedule_id: Mapped[intpk]
    user_id: Mapped[int]
    drug_name: Mapped[str_256] = mapped_column(String(256))
    rec_frequency: Mapped[int]
    duration: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    created_at: Mapped[created_at]