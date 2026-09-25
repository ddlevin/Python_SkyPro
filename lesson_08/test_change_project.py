import uuid
from project_api import ProjectAPI


def test_update_project_positive(base_url, headers, created_project):
    api = ProjectAPI(base_url, headers)
    project_id = created_project["id"]
    new_title = f"Updated Project {uuid.uuid4().hex[:8]}"
    response = api.update_project(project_id, new_title)
    assert response.status_code == 200, (
        f"Ожидался 200, получен {response.status_code}: {response.text}"
    )


def test_update_project_negative_invalid_id(base_url, headers):
    api = ProjectAPI(base_url, headers)
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = api.update_project(fake_id, "New Title")
    assert response.status_code in [404], (
        f"Ожидался 404, получен {response.status_code}: {response.text}"
    )
