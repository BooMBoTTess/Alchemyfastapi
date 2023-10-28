from fastapi.testclient import TestClient

from src.main import app
client = TestClient(app)

def test_read_departments():
    response = client.get('/info')
    assert response.status_code == 200

def test_read_exist_departments():
    for i in range(0,4):
        response = client.get('/info/0')
        assert response.status_code == 200


test_read_departments()
test_read_exist_departments()
