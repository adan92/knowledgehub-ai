from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).resolve().parents[3]


def get_documents_path() -> Path:
    return get_project_root() / "data" / "documents"


def get_vectorstore_path() -> Path:
    return get_project_root() / "data" / "vectorstore"


def get_document_path(filename: str) -> Path:
    """
    Obtiene la ruta absoluta de un documento del repositorio.
    """
    return get_documents_path() / filename
