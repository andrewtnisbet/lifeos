from sqlalchemy.orm import Session

from app.database.models import Task


class CaptureRepository:

    def create_task(
        self,
        db: Session,
        title: str,
        priority: int,
        energy: str,
        minutes: int,
    ) -> Task:

        task = Task(
            title=title,
            priority=priority,
            estimated_minutes=minutes,
            energy_required=energy,
        )

        db.add(task)
        db.commit()
        db.refresh(task)

        return task