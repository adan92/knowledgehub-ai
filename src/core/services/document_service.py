"""
Servicio encargado de administrar los documentos del repositorio.

Su responsabilidad consiste únicamente en gestionar los archivos
almacenados en data/documents.
"""

from pathlib import Path
from shutil import copyfileobj


class DocumentService:

    def __init__(
            self,
            documents_path: Path,
            index_service
    ):
        self.documents_path = documents_path
        self.index_service = index_service

    def list_documents(self):

        return sorted(
            self.documents_path.glob("*.pdf")
        )

    def exists(self, filename: str):

        return (
            self.documents_path / filename
        ).exists()

    def get_document(self, filename: str):

        document = self.documents_path / filename

        if not document.exists():
            raise FileNotFoundError(filename)

        return document

    def upload(self, upload_file):

        destination = (
            self.documents_path /
            upload_file.filename
        )

        with destination.open("wb") as buffer:
            copyfileobj(
                upload_file.file,
                buffer
            )

        self.index_service.rebuild()

        return destination

    def delete(self, filename: str):

        document = self.get_document(filename)

        document.unlink()

        self.index_service.rebuild()

    def rebuild(self):
        self.index_service.rebuild()
