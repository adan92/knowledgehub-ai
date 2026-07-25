"""
Modelo que representa la información asociada a un documento
dentro del KnowledgeHub.

Centraliza los metadatos utilizados por el pipeline RAG y por
la interfaz gráfica para mostrar las fuentes consultadas.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class DocumentMetadata:
    """
    Metadatos de un fragmento de documento.
    """

    document_id: str
    filename: str
    filepath: str
    page: int
    chunk_id: int
    total_chunks: int