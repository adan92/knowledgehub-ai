from dataclasses import dataclass
from pathlib import Path
from typing import List

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


@dataclass
class LoadedDocument:
    filename: str
    documents: list[Document]


class PDFLoaderService:

    def __init__(self, documents_path: Path):
        self.documents_path = documents_path

    def get_pdf_files(self) -> list[Path]:
        return list(self.documents_path.glob("*.pdf"))

    def load_documents(self) -> list[LoadedDocument]:
        loaded_documents = []
        for pdf_path in self.get_pdf_files():
            try:
                loader = PyPDFLoader(str(pdf_path))
                loaded_documents.append(LoadedDocument(
                    filename=pdf_path.name,
                    documents=loader.load()
                ))
            except Exception as e:

                print(f"Error cargando {pdf_path.name}: {e}")

        return loaded_documents
