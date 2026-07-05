from pydantic import BaseModel
from enum import Enum
from app.shared.enums import EnergyLevel, Responsibility


class CaptureRequest(BaseModel):
    text: str


class TaskClassification(BaseModel):

    title: str

    priority: int

    estimated_minutes: int

    energy_required: EnergyLevel

    must_schedule: bool

    responsibility: Responsibility


    confidence: float

