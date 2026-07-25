import requests

from config.settings import settings


class DocumentClient:

    def __init__(self):

        self.base_url = (
            f"{settings.api_base_url}/documents"
        )

    def list_documents(self):

        response = requests.get(
            self.base_url
        )

        response.raise_for_status()

        return response.json()

    def upload(self, uploaded_file):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file,
                "application/pdf"
            )
        }

        response = requests.post(
            self.base_url,
            files=files
        )

        response.raise_for_status()

    def delete(self, filename):

        response = requests.delete(
            f"{self.base_url}/{filename}"
        )

        response.raise_for_status()

    def rebuild(self):

        response = requests.post(
            f"{self.base_url}/reindex"
        )

        response.raise_for_status()
