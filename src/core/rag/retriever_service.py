"""
Retriever Service.

Este módulo implementa la capa de recuperación de información del
pipeline Retrieval-Augmented Generation (RAG).

Su responsabilidad consiste en consultar el índice vectorial mediante
búsquedas semánticas para recuperar los fragmentos de texto más
relevantes según la consulta realizada por el usuario.

Actualmente se utiliza la estrategia Max Marginal Relevance (MMR), la
cual busca equilibrar la relevancia de los resultados con la diversidad
de la información recuperada.

Proyecto:
    KnowledgeHub AI
"""
from langchain_core.documents import Document


class RetrieverService:
    """
    Servicio responsable de recuperar información relevante desde el
    índice vectorial.

    Este servicio encapsula las operaciones de búsqueda sobre el vector
    store utilizado por la aplicación.

    En lugar de realizar búsquedas por coincidencia exacta, emplea
    similitud semántica mediante embeddings, permitiendo localizar
    información relacionada con la intención de la consulta del usuario.

    Attributes:
        vector_store:
            Índice vectorial utilizado para realizar búsquedas
            semánticas sobre los documentos procesados.
    """

    def __init__(self, vector_store):
        self.vector_store = vector_store

    def search(self, question: str, k: int = 12, fetch: int = 20) -> list[Document]:
        """Recupera hasta ``k`` chunks para una pregunta.

        ``fetch`` amplía el conjunto candidato antes de aplicar diversidad MMR.
        """
        return self.vector_store.max_marginal_relevance_search(
            query=question,
            k=k,
            fetch_k=fetch
        )
