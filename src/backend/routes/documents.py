"""
Endpoints para la administración de documentos.

Esta ruta expone las operaciones necesarias para gestionar la Base de
Conocimiento de KnowledgeHub AI.
"""

from fastapi import (
    APIRouter,
    File,
    HTTPException,
    UploadFile
)
from fastapi.responses import FileResponse

from core.embeddings.embedding_service import EmbeddingService
from core.services.document_service import DocumentService
from core.services.index_service import IndexService
from core.utils.path_utils import get_documents_path

router = APIRouter()

# ---------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------

embedding_model = (
    EmbeddingService()
    .get_embedding_model()
)

index_service = IndexService(
    embedding_model
)

document_service = DocumentService(
    documents_path=get_documents_path(),
    index_service=index_service
)


# ---------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------

@router.get("")
def list_documents():
    """
    Obtiene la lista de documentos disponibles.
    """

    return [
        document.name
        for document in document_service.list_documents()
    ]


@router.get("/{filename}")
def get_document(filename: str):
    """
    Descarga un documento.
    """

    try:

        document = document_service.get_document(
            filename
        )

        return FileResponse(
            path=document,
            media_type="application/pdf",
            filename=document.name
        )

    except FileNotFoundError:

        raise HTTPException(
            status_code=404,
            detail="Documento no encontrado."
        )


@router.post("")
def upload_document(
        file: UploadFile = File(...)
):
    """
    Sube un documento y reconstruye automáticamente el índice vectorial.
    """

    if not file.filename.lower().endswith(".pdf"):

        raise HTTPException(
            status_code=400,
            detail="Solo se permiten archivos PDF."
        )

    document_service.upload(file)

    return {
        "message": "Documento cargado correctamente."
    }


@router.delete("/{filename}")
def delete_document(filename: str):
    """
    Elimina un documento y reconstruye automáticamente el índice vectorial.
    """

    try:

        document_service.delete(filename)

        return {
            "message": "Documento eliminado correctamente."
        }

    except FileNotFoundError:

        raise HTTPException(
            status_code=404,
            detail="Documento no encontrado."
        )


@router.post("/reindex")
def rebuild_index():
    """
    Fuerza la reconstrucción completa del índice vectorial.
    """

    index_service.rebuild()

    return {
        "message": "Índice reconstruido correctamente."
    }
