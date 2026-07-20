from pathlib import Path

from langchain_community.vectorstores import FAISS


class FAISSStore:
    """
    Encargado únicamente de crear,
    guardar y cargar el Vector Store.
    """

    def __init__(self, embedding_model):
        self.embedding_model = embedding_model

    def create_vector_store(self, documents):
        return FAISS.from_documents(
            documents=documents,
            embedding=self.embedding_model
        )

    def save(self, vector_store, save_path: Path):

        save_path.mkdir(parents=True, exist_ok=True)

        vector_store.save_local(str(save_path))

    def load(self, save_path: Path):

        return FAISS.load_local(
            folder_path=str(save_path),
            embeddings=self.embedding_model,
            allow_dangerous_deserialization=True
        )