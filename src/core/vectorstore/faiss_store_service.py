"""
FAISS Vector Store.

Este módulo implementa la capa de persistencia del índice vectorial
utilizado por KnowledgeHub AI.

Su responsabilidad consiste en crear, almacenar y recuperar el índice
FAISS que contiene las representaciones vectoriales (embeddings) de los
documentos procesados.

Al centralizar estas operaciones en un único servicio, el resto de la
aplicación permanece desacoplado de la implementación específica del
vector store, facilitando futuras migraciones hacia otras soluciones
como ChromaDB, Pinecone o Milvus.

Proyecto:
    KnowledgeHub AI
"""

from langchain_community.vectorstores import FAISS


class FAISSStoreService:
    """
    Servicio encargado de administrar el índice vectorial FAISS.

    Esta clase encapsula las operaciones necesarias para crear,
    almacenar y cargar el índice vectorial utilizado durante el flujo
    Retrieval-Augmented Generation (RAG).

    El índice almacena los embeddings generados a partir de los
    documentos procesados, permitiendo realizar búsquedas semánticas de
    forma eficiente.

    Attributes:
        embedding_model:
            Modelo de embeddings utilizado para generar y reconstruir
            las representaciones vectoriales del índice.
    """

    def __init__(self, embedding_model):
        """
        Inicializa el servicio del vector store.

        Args:
            embedding_model:
                Modelo de embeddings utilizado por FAISS para indexar y
                consultar documentos.
        """
        self.embedding_model = embedding_model

    def create_vector_store(self, documents):
        """
        Crea un nuevo índice vectorial a partir de una colección de documentos.

        Args:
            documents:
                Lista de documentos previamente procesados y divididos
                en fragmentos (chunks).

        Returns:
            FAISS:
                Índice vectorial listo para realizar búsquedas
                semánticas.
        """
        return FAISS.from_documents(
            documents,
            self.embedding_model
        )

    @staticmethod
    def save(vector_store, path):
        """
        Guarda el índice vectorial en el sistema de archivos.

        Args:
            vector_store:
                Instancia del índice FAISS a persistir.

            path:
                Ruta donde será almacenado el índice.
        """
        vector_store.save_local(path)

    def load(self, path):
        """
        Carga un índice vectorial previamente almacenado.

        Args:
            path:
                Ruta donde se encuentra el índice persistido.

        Returns:
            FAISS:
                Índice vectorial listo para ser utilizado durante las
                búsquedas semánticas.

        Notes:
            Se habilita la deserialización debido a que el índice es
            generado y consumido exclusivamente por la propia aplicación.
        """
        return FAISS.load_local(
            path,
            self.embedding_model,
            allow_dangerous_deserialization=True
        )
