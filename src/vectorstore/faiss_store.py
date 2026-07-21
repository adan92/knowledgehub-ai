from langchain_community.vectorstores import FAISS


class FAISSStore:

    def __init__(self, embedding_model):

        self.embedding_model = embedding_model

    def create_vector_store(self, documents):

        return FAISS.from_documents(
            documents,
            self.embedding_model
        )

    def save(self, vector_store, path):

        vector_store.save_local(path)

    def load(self, path):

        return FAISS.load_local(
            path,
            self.embedding_model,
            allow_dangerous_deserialization=True
        )