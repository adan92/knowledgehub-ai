"""
Servicio encargado de administrar el índice vectorial.

Su responsabilidad consiste en crear, cargar y reconstruir el índice
FAISS utilizado por el pipeline RAG.
"""

from pathlib import Path

from core.loaders.pdf_loader import PDFLoaderService
from core.processing.document_processor import DocumentProcessor
from core.utils.path_utils import (
    get_documents_path,
    get_vectorstore_path
)
from core.vectorstore.faiss_store_service import FAISSStoreService


class IndexService:

    def __init__(self, embedding_model):

        self.loader = PDFLoaderService(
            get_documents_path()
        )

        self.processor = DocumentProcessor()

        self.faiss = FAISSStoreService(
            embedding_model
        )
        self.vector_store = None

    def load_or_create(self):
        """
        Carga el índice existente o lo crea si aún no existe.
        """

        if self.__vector_store_exists():
            self.vector_store = self.load()
        else:
            self.vector_store = self.rebuild()

        return self.vector_store

    def load(self):
        """
        Carga el índice vectorial desde disco.
        """

        print("Vector Store encontrado.")
        print("Cargando índice existente...")

        return self.faiss.load(
            get_vectorstore_path()
        )

    def rebuild(self):
        """
        Reconstruye completamente el índice vectorial a partir de todos
        los documentos disponibles.
        """

        print("Reconstruyendo Vector Store...")

        documents = self.loader.load_documents()

        all_chunks = []

        for document in documents:

            chunks = self.processor.process(
                document.filename,
                document.documents
            )

            all_chunks.extend(chunks)

            print(
                f"{document.filename}: {len(chunks)} chunks"
            )

        if not all_chunks:
            raise ValueError(
                "No se encontraron fragmentos para indexar. "
                "Agrega al menos un PDF válido en data/documents."
            )

        print(f"Total de chunks: {len(all_chunks)}")

        vector_store = self.faiss.create_vector_store(all_chunks)

        self.faiss.save(
            vector_store,
            get_vectorstore_path()
        )

        print("Vector Store creado correctamente.")

        return vector_store

    @staticmethod
    def __vector_store_exists() -> bool:
        """
        Comprueba que existan los archivos del índice FAISS.
        """

        vectorstore_path = Path(
            get_vectorstore_path()
        )

        return (
            (vectorstore_path / "index.faiss").exists()
            and
            (vectorstore_path / "index.pkl").exists()
        )
