from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String
from datetime import datetime
from typing import Annotated

from sqlalchemy import text, Integer
from sqlalchemy.orm import mapped_column



# UUIDPrimaryKey = Annotated[uuid.UUID, mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)]
intpk = Annotated[int, mapped_column(Integer, primary_key=True, autoincrement=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))] # TODO: упростить created_at
str_256 = Annotated[str, 256]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }




