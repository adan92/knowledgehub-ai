"""
LLM Service.

Este módulo centraliza la creación del Modelo de Lenguaje Grande (LLM)
utilizado por KnowledgeHub AI para generar respuestas a partir del
contexto recuperado durante el flujo Retrieval-Augmented Generation
(RAG).

Actualmente se utiliza Gemini Flash mediante la integración oficial de
LangChain con Google Generative AI.

La existencia de este servicio desacopla el resto de la aplicación del
proveedor específico del modelo, facilitando futuras migraciones hacia
otros LLMs.

Proyecto:
    KnowledgeHub AI
"""
from langchain_google_genai import ChatGoogleGenerativeAI

from config.settings import settings


class LLMService:
    """
    Servicio encargado de crear instancias del modelo de lenguaje.

    Esta clase actúa como una fábrica (Factory) para inicializar el LLM
    utilizado por la aplicación.

    Centralizar esta responsabilidad permite modificar fácilmente el
    modelo, la temperatura o cualquier otro parámetro de generación sin
    afectar a los servicios consumidores.
    """

    @staticmethod
    def create():

        return ChatGoogleGenerativeAI(
            model="models/gemini-flash-latest",
            temperature=0,
            api_key=settings.google_api_key
        )
