from sqlalchemy.orm import Session

from app.database.models import Task


class CaptureRepository:

    def create_task(
        self,
        db: Session,
        title: str,
        priority: int,
        energy: str,
        minutes: int
    ):

        task = Task(
            title=title,
            priority=priority,
            energy_required=energy,
            estimated_minutes=minutes
        )

        db.add(task)

        db.commit()

        db.refresh(task)

        return task