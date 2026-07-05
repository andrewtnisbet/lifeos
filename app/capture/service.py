from app.capture.classifiers.factory import get_classifier
from app.capture.repository import CaptureRepository


class CaptureService:

    def __init__(self):
        self.repo = CaptureRepository()

    def process(
        self,
        db,
        text: str
    ):

        classifier = get_classifier()

        classification = classifier.classify(text)

        task = self.repo.create_task(
            db=db,
            title=classification.title,
            priority=classification.priority,
            energy=classification.energy_required,
            minutes=classification.estimated_minutes,
)

        return {
            "task_id": str(task.id),
            "status": "created"
        }