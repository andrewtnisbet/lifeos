from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import UUID

import uuid
import datetime


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    title: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String,
        default="open"
    )

    priority: Mapped[int] = mapped_column(
        Integer,
        default=5
    )

    estimated_minutes: Mapped[int] = mapped_column(
        Integer,
        nullable=True
    )

    energy_required: Mapped[str] = mapped_column(
        String,
        nullable=True
    )

    can_split: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    must_schedule: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )