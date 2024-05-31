import pytest
from Backend.app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'vacZWER' in response.data  # Обновленный текст, который должен присутствовать в HTML
