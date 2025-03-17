from config.models import Base, intpk
from sqlalchemy.orm import Mapped

class UsersOrm(Base):
    __tablename__ = 'users'
    user_id: Mapped[intpk]