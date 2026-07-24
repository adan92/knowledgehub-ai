"""
Servicio encargado del procesamiento de documentos.

Convierte los documentos cargados en fragmentos (chunks) utilizando
RecursiveCharacterTextSplitter para optimizar la recuperación de
información durante el proceso RAG.
"""
import hashlib
from pathlib import Path

from core.models import DocumentMetadata
from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentProcessor:

    def __init__(
            self,
            chunk_size: int = 1000,
            chunk_overlap: int = 200
    ):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def process(self, filename: str, pages):
        """
          Divide un documento en fragmentos y agrega metadatos.

          Cada chunk conserva información del documento original para que
          posteriormente sea posible mostrar las fuentes utilizadas por el
          modelo.

          Los metadatos incluyen:

          - filename
          - chunk_id
          - total_chunks

          Args:
              filename:
                  Nombre del documento.

              pages:
                  Páginas obtenidas desde PyPDFLoader.

          Returns:
              Lista de fragmentos procesados.
          """
        chunks = self.text_splitter.split_documents(pages)
        document_id = hashlib.sha256(
            filename.encode("utf-8")
        ).hexdigest()

        filepath = str(
            Path("data")
            / "documents"
            / filename
        )

        total_chunks = len(chunks)

        for index, chunk in enumerate(chunks):
            metadata = DocumentMetadata(
                document_id=document_id,
                filename=filename,
                filepath=filepath,
                page=chunk.metadata.get("page", 0) + 1,
                chunk_id=index,
                total_chunks=total_chunks
            )

            chunk.metadata.update(metadata.__dict__)

        return chunks
