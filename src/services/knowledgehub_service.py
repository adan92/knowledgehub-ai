from pathlib import Path

from embeddings.embedding_service import EmbeddingService
from llm.llm_service import LLMService
from loaders.pdf_loader import PDFLoaderService
from processing.document_processor import DocumentProcessor
from rag.rag_service import RAGService
from rag.retriever_service import RetrieverService
from utils.path_utils import (
    get_documents_path,
    get_vectorstore_path
)
from vectorstore.faiss_store import FAISSStore


class KnowledgeHubService:

    def __init__(self):

        self.loader = PDFLoaderService(
            get_documents_path()
        )

        self.processor = DocumentProcessor()

        self.embedding_service = EmbeddingService()

        self.embedding_model = (
            self.embedding_service.get_embedding_model()
        )

        self.faiss = FAISSStore(
            self.embedding_model
        )

        self.vector_store = (
            self.__initialize_vector_store()
        )

        self.retriever = RetrieverService(
            self.vector_store
        )

        self.llm = LLMService().create()

        self.rag = RAGService(
            self.retriever,
            self.llm
        )

    def ask(self, question: str):

        return self.rag.ask(question)

    # --------------------------------------------------------
    # Métodos privados
    # --------------------------------------------------------

    def __initialize_vector_store(self):

        if self.__vector_store_exists():
            return self.__load_vector_store()

        return self.__create_vector_store_from_documents()

    @staticmethod
    def __vector_store_exists() -> bool:

        vectorstore_path = Path(
            get_vectorstore_path()
        )

        return (
            (vectorstore_path / "index.faiss").exists()
            and
            (vectorstore_path / "index.pkl").exists()
        )

    def __load_vector_store(self):

        print("Vector Store encontrado.")
        print("Cargando índice existente...")

        return self.faiss.load(
            get_vectorstore_path()
        )

    def __create_vector_store_from_documents(self):

        print("No existe un Vector Store.")
        print("Iniciando proceso de indexación...")

        documents = self.loader.load_documents()

        all_chunks = []

        for document in documents:

            chunks = self.processor.process(
                document.filename,
                document.documents
            )

            all_chunks.extend(chunks)

            print(
                f"{document.filename}: "
                f"{len(chunks)} chunks"
            )

        print()

        print(
            f"Total de chunks: {len(all_chunks)}"
        )

        vector_store = self.faiss.create_vector_store(
            all_chunks
        )

        self.faiss.save(
            vector_store,
            get_vectorstore_path()
        )

        print("Vector Store creado correctamente.")

        return vector_store
