from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch


client = TestClient(app)


def test_capture_endpoint():

    with patch(
        "app.capture.routes.service.process"
    ) as mock_process:

        mock_process.return_value = {
            "task_id": "fake-uuid",
            "status": "created"
        }

        response = client.post(
            "/capture",
            json={
                "text": "Update resume"
            }
        )

        assert response.status_code == 200

        assert response.json()["status"] == "created"