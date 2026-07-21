from langchain_core.documents import Document


class RetrieverService:

    def __init__(self, vector_store):
        self.vector_store = vector_store

    def search(self, question: str, k: int = 3) -> list[Document]:

        return self.vector_store.similarity_search(
            query=question,
            k=k
        )