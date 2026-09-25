import requests


class ProjectAPI:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def create_project(self, title):
        """POST /api-v2/projects — создание проекта."""
        payload = {"title": title}
        return requests.post(
            f"{self.base_url}/projects",
            json=payload,
            headers=self.headers
        )

    def update_project(self, project_id, title):
        """PUT /api-v2/projects/{id} — обновление проекта."""
        payload = {"title": title}
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=payload,
            headers=self.headers
        )

    def get_project(self, project_id):
        """GET /api-v2/projects/{id} — получение проекта."""
        return requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )
