#import streamlit as st
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter

from embeddings.embedding_service import EmbeddingService
from loaders.pdf_loader import PDFLoaderService
from processing.document_processor import DocumentProcessor
from utils.path_utils import get_documents_path, get_vectorstore_path
from vectorstore.faiss_store import FAISSStore

#st.title("KnowledgeHub AI")
#st.write("Welcome!")
load_dotenv()


loader = PDFLoaderService(
    get_documents_path()
)

documents = loader.load_documents()
all_chunks = []
processor = DocumentProcessor()
for document in documents:

    chunks = processor.process(
        document.filename,
        document.documents
    )

    all_chunks.extend(chunks)

    print(f"{document.filename}")
    print(f"Chunks: {len(chunks)}")

print("--------------------------------")
print(f"Total de chunks: {len(all_chunks)}")
print("--------------------------------")

embedding_service = EmbeddingService()

embedding_model = embedding_service.get_embedding_model()

faiss_service = FAISSStore(embedding_model)

vector_store = faiss_service.create_vector_store(all_chunks)

faiss_service.save(
    vector_store,
    get_vectorstore_path()
)

print("Vector Store creado correctamente.")

results = vector_store.similarity_search(
    "¿Qué es un Post-Mortem?",
    k=3
)

for doc in results:
    print(doc.metadata)
    print(doc.page_content)
    print("-" * 80)