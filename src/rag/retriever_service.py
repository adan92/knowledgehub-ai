from langchain_core.documents import Document


class RetrieverService:

    def __init__(self, vector_store):
        self.vector_store = vector_store

    def search(self, question: str, k: int = 12,fetch: int=20) -> list[Document]:

        return self.vector_store.max_marginal_relevance_search(
            query=question,
            k=k,
            fetch_k=fetch
        )