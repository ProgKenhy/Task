from sqlalchemy import ForeignKey, String
from sqlalchemy.testing.schema import mapped_column

from config.models import Base, str_256, intpk, created_at
from sqlalchemy.orm import Mapped

class ScheduleOrm(Base):
    __tablename__ = 'schedules'
    schedule_id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id', ondelete='CASCADE'))
    drug_name: Mapped[str_256] = mapped_column(String(256))
    rec_frequency: Mapped[int]
    duration: Mapped[int]
    created_at: Mapped[created_at]