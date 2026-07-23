"""
Servicios para la carga de documentos PDF.

Este módulo contiene las clases encargadas de descubrir y cargar los
documentos PDF almacenados en el directorio de conocimiento de
KnowledgeHub AI.

Los documentos son cargados utilizando PyPDFLoader de LangChain y
posteriormente procesados por el pipeline RAG.

Autor:
    Christian Amezcua Aguilar

Proyecto:
    KnowledgeHub AI
"""
from dataclasses import dataclass
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


@dataclass
class LoadedDocument:
    """
    Representa un documento cargado desde el sistema de archivos.

    Attributes:
        filename:
            Nombre del archivo PDF.

        documents:
            Lista de páginas cargadas como objetos Document de LangChain.
    """
    filename: str
    documents: list[Document]


class PDFLoaderService:
    """
    Servicio responsable de cargar documentos PDF.

    Esta clase centraliza la lectura de archivos PDF desde el directorio
    configurado y devuelve su contenido listo para ser procesado por
    el pipeline RAG.

    Attributes:
        documents_path:
            Ruta donde se almacenan los documentos PDF.
    """

    def __init__(self, documents_path: Path):
        """
        Inicializa el cargador de documentos.

        Args:
            documents_path:
                Directorio que contiene los archivos PDF.
        """
        self.documents_path = documents_path

    def get_pdf_files(self) -> list[Path]:
        """
        Obtiene todos los archivos PDF disponibles.

        Returns:
            Lista con las rutas de cada documento encontrado.
        """

        return list(self.documents_path.glob("*.pdf"))

    def load_documents(self) -> list[LoadedDocument]:
        """
        Carga todos los documentos PDF encontrados.

        Cada archivo es procesado mediante PyPDFLoader y encapsulado en
        un objeto LoadedDocument para conservar tanto su contenido como
        el nombre del archivo de origen.

        Returns:
            Lista de documentos cargados.
        """
        loaded_documents = []
        for pdf_path in self.get_pdf_files():
            try:
                loader = PyPDFLoader(str(pdf_path))
                loaded_documents.append(LoadedDocument(
                    filename=pdf_path.name,
                    documents=loader.load()
                ))
            except Exception as e:

                print(f"Error cargando {pdf_path.name}: {e}")

        return loaded_documents
