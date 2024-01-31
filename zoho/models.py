from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Preset(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    date: datetime = Field(default_factory=datetime.utcnow)
    distance: int
