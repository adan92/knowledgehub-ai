from langchain_google_genai import ChatGoogleGenerativeAI


class LLMService:

    @staticmethod
    def create():

        return ChatGoogleGenerativeAI(
            model="models/gemini-flash-latest",
            temperature=0
        )