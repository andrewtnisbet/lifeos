from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.capture.schemas import CaptureRequest
from app.capture.service import CaptureService
from app.database.dependencies import get_db


router = APIRouter()

service = CaptureService()


@router.post("/capture")

def capture(
    request: CaptureRequest,
    db: Session = Depends(get_db)
):

    return service.process(
        db=db,
        text=request.text
    )