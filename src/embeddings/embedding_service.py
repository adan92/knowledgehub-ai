from langchain_cohere import CohereEmbeddings


class EmbeddingService:

    def __init__(self):
        self.embedding_model = CohereEmbeddings(
            model="embed-multilingual-v3.0"
        )

    def get_embedding_model(self):
        return self.embedding_model