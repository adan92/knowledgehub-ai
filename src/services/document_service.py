"""
Servicio encargado de administrar los documentos del repositorio.

Su responsabilidad consiste únicamente en gestionar los archivos
almacenados en data/documents.
"""

from pathlib import Path


class DocumentService:

    def __init__(self, documents_path: Path):
        self.documents_path = documents_path

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
    