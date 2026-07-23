"""
Embedding Service.

Este módulo proporciona el servicio encargado de inicializar y exponer
el modelo de embeddings utilizado por KnowledgeHub AI.

Los embeddings permiten convertir texto en representaciones vectoriales
que posteriormente son almacenadas y consultadas mediante un índice
vectorial (FAISS), facilitando la búsqueda semántica durante el proceso
Retrieval-Augmented Generation (RAG).

Actualmente se utiliza el modelo multilingüe de Cohere, optimizado para
la representación semántica de documentos en distintos idiomas.

Proyecto:
    KnowledgeHub AI
"""
from langchain_cohere import CohereEmbeddings


class EmbeddingService:
    """
    Servicio responsable de proporcionar el modelo de embeddings.

    Esta clase centraliza la creación del modelo utilizado para generar
    representaciones vectoriales de documentos y consultas.

    Al encapsular la inicialización del modelo en un único servicio,
    resulta sencillo sustituir el proveedor de embeddings sin afectar
    el resto de la arquitectura de la aplicación.

    Attributes:
        embedding_model (CohereEmbeddings):
            Instancia del modelo de embeddings utilizada por el sistema.
    """
    def __init__(self):
        self.embedding_model = CohereEmbeddings(
            model="embed-multilingual-v3.0"
        )

    def get_embedding_model(self):
        return self.embedding_model
