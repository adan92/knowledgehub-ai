from langchain_core.messages import HumanMessage


class RAGService:

    def __init__(self, retriever, llm):

        self.retriever = retriever
        self.llm = llm

    def ask(self, question: str):

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

        return {
            "answer": response.content,
            "documents": documents
        }