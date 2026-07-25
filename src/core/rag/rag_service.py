"""
Implementación del flujo Retrieval-Augmented Generation (RAG).

El servicio ejecuta las siguientes etapas:

1. Recuperación de documentos relevantes.
2. Construcción del contexto.
3. Generación del prompt.
4. Consulta al modelo Gemini.
5. Devolución de la respuesta junto con las fuentes.

El modelo únicamente responde utilizando el contexto recuperado,
reduciendo alucinaciones.
"""
from langchain_core.messages import HumanMessage


class RAGService:

    def __init__(self, retriever, llm):

        self.retriever = retriever
        self.llm = llm

    def ask(self, question: str):
        """Responde una pregunta y devuelve también los documentos recuperados."""
        documents = self.retriever.search(question)

        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        prompt = f"""
                Eres un asistente experto.

                Responde únicamente utilizando la información proporcionada.
                
                Si la respuesta no está presente en el contexto responde:
                
                "No encontré información suficiente en los documentos."
                
                Contexto:
                
                {context}
                
                Pregunta:
                
                {question}
                """

        response = self.llm.invoke(
            [HumanMessage(content=prompt)]
        )
        answer = response.text
        return {
            "answer": answer,
            "documents": documents
        }
