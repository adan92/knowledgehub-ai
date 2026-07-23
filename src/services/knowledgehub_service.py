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

from embeddings.embedding_service import EmbeddingService
from llm.llm_service import LLMService
from loaders.pdf_loader import PDFLoaderService
from models.source import Source
from processing.document_processor import DocumentProcessor
from rag.rag_service import RAGService
from rag.retriever_service import RetrieverService
from utils.path_utils import (
    get_documents_path,
    get_vectorstore_path
)
from vectorstore.faiss_store_service import FAISSStoreService


class KnowledgeHubService:
    """Inicializa la indexación, recuperación y generación de respuestas.

    Si ya existe un índice en disco se reutiliza; en caso contrario, los PDF
    se cargan, fragmentan, vectorizan y persisten durante la inicialización.
    """
    def __init__(self):
        self.loader = PDFLoaderService(get_documents_path())
        self.processor = DocumentProcessor()
        self.embedding_service = EmbeddingService()
        self.embedding_model = self.embedding_service.get_embedding_model()
        self.faiss = FAISSStoreService(self.embedding_model)
        self.vector_store = self.__initialize_vector_store()
        self.retriever = RetrieverService(self.vector_store)
        self.llm = LLMService().create()
        self.rag = RAGService(self.retriever, self.llm)

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

    def __initialize_vector_store(self):
        """Carga el índice persistido o construye uno nuevo desde los PDF."""
        if self.__vector_store_exists():
            return self.__load_vector_store()
        return self.__create_vector_store_from_documents()

    @staticmethod
    def __vector_store_exists() -> bool:
        """Comprueba que existan los dos archivos requeridos por FAISS."""
        vectorstore_path = Path(get_vectorstore_path())
        return (
                (vectorstore_path / "index.faiss").exists()
                and (vectorstore_path / "index.pkl").exists()
        )

    def __load_vector_store(self):
        """Restaura el índice vectorial existente."""
        print("Vector Store encontrado.")
        print("Cargando índice existente...")
        return self.faiss.load(get_vectorstore_path())

    def __create_vector_store_from_documents(self):
        """Construye y guarda el índice a partir de todos los PDF disponibles."""
        print("No existe un Vector Store.")
        print("Iniciando proceso de indexación...")
        documents = self.loader.load_documents()
        all_chunks = []

        for document in documents:
            chunks = self.processor.process(document.filename, document.documents)
            all_chunks.extend(chunks)
            print(f"{document.filename}: {len(chunks)} chunks")

        if not all_chunks:
            raise ValueError(
                "No se encontraron fragmentos para indexar. "
                "Agrega al menos un PDF válido en data/documents."
            )

        print(f"Total de chunks: {len(all_chunks)}")
        vector_store = self.faiss.create_vector_store(all_chunks)
        self.faiss.save(vector_store, get_vectorstore_path())
        print("Vector Store creado correctamente.")
        return vector_store

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
                    page=metadata["page"]
                )
            )

        return sources
