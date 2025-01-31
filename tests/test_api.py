from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_process_receipt():
    response = client.post(
        "/receipts/process",
        json={
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [{"shortDescription": "Mountain Dew", "price": "6.49"}],
            "total": "6.49"
        }
    )
    assert response.status_code == 200
    assert "id" in response.json()