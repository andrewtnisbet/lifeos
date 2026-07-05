from abc import ABC
from abc import abstractmethod

from app.capture.schemas import TaskClassification


class BaseClassifier(ABC):

    @abstractmethod
    async def classify(
        self,
        text: str
    ) -> TaskClassification:
        ...