from fastapi import FastAPI
from app.capture.routes import router as capture_router

app = FastAPI()

app.include_router(capture_router)

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
