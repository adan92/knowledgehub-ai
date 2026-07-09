#import streamlit as st
from langchain_text_splitters import RecursiveCharacterTextSplitter

#st.title("KnowledgeHub AI")

#st.write("Welcome!")

from loaders import pdf_loader

all_loaded_documents=pdf_loader.load_pdf()

for pdf_loaded in all_loaded_documents:
    nombre_archivo = pdf_loaded['archivo']
    pages = pdf_loaded['documentos']
    total_caracteres = sum(len(pagina.page_content) for pagina in pages)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(pages)
    print(f"Documento leído: {nombre_archivo}")
    print(f"Numero de paginas: {len(pages)}")
    print(f"Caracteres: {total_caracteres}")
    print(f"Chunks creados: {len(chunks)}")
    print("\nPrimer chunk:")
    print("-" * 40)
    if chunks:
        print(chunks[0].page_content)
    else:
        print("No se generaron chunks.")
    print("-" * 40)
