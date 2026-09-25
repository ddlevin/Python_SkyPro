import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    return "https://ru.yougile.com/api-v2"


@pytest.fixture(scope="session")
def token():
    # Наставнику: укажите API-ключ YouGile
    return "Api_Key"


@pytest.fixture(scope="session")
def headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


@pytest.fixture(scope="session")
def created_project(base_url, headers):
    """Создаёт проект для тестов и удаляет его после (если API позволяет)."""
    payload = {"title": "Test Project Fixture"}
    response = requests.post(
        f"{base_url}/projects",
        json=payload,
        headers=headers
    )
    project_id = response.json().get("id")
    yield {"id": project_id, "response": response}
