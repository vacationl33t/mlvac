import pytest
from model.app.main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_query(client):
    response = client.post('/query/', json={
        "text": "hi",
    })
    assert response.status_code == 200
    response_json = response.get_json()  # Получаем JSON-ответ
    assert "response" in response_json  # Проверяем, что ключ 'response' есть в JSON-ответе
