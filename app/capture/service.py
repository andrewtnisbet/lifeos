from app.capture.classifier import classify_text
from app.capture.repository import CaptureRepository


class CaptureService:

    def __init__(self):

        self.repo = CaptureRepository()

    def process(
        self,
        db,
        text: str
    ):

        metadata = classify_text(text)

        task = self.repo.create_task(
            db=db,
            title=text,
            priority=metadata["priority"],
            energy=metadata["energy"],
            minutes=metadata["minutes"]
        )

        return {
            "task_id": str(task.id),
            "status": "created"
        }