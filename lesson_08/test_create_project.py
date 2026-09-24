import uuid
from project_api import ProjectAPI


def test_create_project_positive(base_url, headers):
    api = ProjectAPI(base_url, headers)
    unique_title = f"Test Project {uuid.uuid4().hex[:8]}"
    response = api.create_project(unique_title)
    assert response.status_code == 201, (
        f"Ожидался 201, получен {response.status_code}: {response.text}"
    )
    assert "id" in response.json(), "В ответе нет id проекта"


def test_create_project_negative_empty_title(base_url, headers):
    api = ProjectAPI(base_url, headers)
    response = api.create_project("")
    assert response.status_code in [400, 422], (
        f"Ожидался 400/422, получен {response.status_code}: {response.text}"
    )
