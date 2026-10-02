from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_document_chunks():
    data=client.post("/v1/run",json={"value":"Title\n\nBody"}).json()
    assert data["blocks"]==2
    assert data["chunks"][0]["citation"].startswith("page:1")
