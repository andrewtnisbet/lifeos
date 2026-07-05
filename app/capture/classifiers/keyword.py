from app.capture.classifiers.base import BaseClassifier
from app.capture.schemas import TaskClassification
from app.shared.enums import EnergyLevel, Responsibility


class KeywordClassifier(BaseClassifier):

    def classify(self, text: str) -> TaskClassification:
        return TaskClassification(
            title=text,
            priority=5,
            estimated_minutes=15,
            energy_required=EnergyLevel.MEDIUM,
            must_schedule=False,
            responsibility=Responsibility.PERSONAL,
            confidence=0.30,
        )