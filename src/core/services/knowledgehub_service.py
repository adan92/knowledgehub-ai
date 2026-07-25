"""
Servicio principal de KnowledgeHub AI.

Esta clase actúa como fachada de la aplicación y coordina todos los
componentes del sistema RAG.

Su responsabilidad consiste en:

- cargar documentos
- procesarlos
- construir o cargar el índice FAISS
- inicializar el modelo de embeddings
- inicializar el modelo LLM
- atender consultas del usuario

Gracias a esta clase, la interfaz no necesita conocer detalles sobre
la implementación interna del pipeline.
"""
from pathlib import Path

from core.embeddings.embedding_service import EmbeddingService
from core.llm.llm_service import LLMService
from core.models.source import Source
from core.rag.rag_service import RAGService
from core.rag.retriever_service import RetrieverService
from core.services.index_service import IndexService


class KnowledgeHubService:
    """Inicializa la indexación, recuperación y generación de respuestas.

    Si ya existe un índice en disco se reutiliza; en caso contrario, los PDF
    se cargan, fragmentan, vectorizan y persisten durante la inicialización.
    """

    def __init__(self):
        self.embedding_service = EmbeddingService()

        self.embedding_model = (
            self.embedding_service.get_embedding_model()
        )

        self.index_service = IndexService(
            self.embedding_model
        )

        self.index_service.load_or_create()

        self.retriever = RetrieverService(
            self.index_service
        )

        self.llm = LLMService().create()

        self.rag = RAGService(
            self.retriever,
            self.llm
        )

    def ask(self, question: str):
        """Delega la consulta al flujo RAG ya inicializado."""
        result = self.rag.ask(question)
        sources = self.__build_sources(
            result["documents"]
        )

        return {
            "answer": result["answer"],
            "sources": sources
        }

    @staticmethod
    def __build_sources(documents) -> list[Source]:
        """
        Convierte los documentos recuperados por el RAG en
        fuentes listas para ser utilizadas por la interfaz.
        """

        sources = []
        rendered = set()

        for document in documents:

            metadata = document.metadata

            key = (
                metadata["filename"],
                metadata["page"]
            )

            if key in rendered:
                continue

            rendered.add(key)

            sources.append(
                Source(
                    document_id=metadata["document_id"],
                    filename=metadata["filename"],
                    filepath=metadata["filepath"],
                    page=metadata["page"],
                    content=document.page_content
                )
            )

        return sources
