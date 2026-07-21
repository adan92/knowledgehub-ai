from langchain_google_genai import ChatGoogleGenerativeAI


class LLMService:

    @staticmethod
    def create():

        return ChatGoogleGenerativeAI(
            model="models/gemini-1.5-flash",
            temperature=0
        )