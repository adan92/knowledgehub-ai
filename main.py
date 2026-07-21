from dotenv import load_dotenv

from services.knowledgehub_service import KnowledgeHubService

load_dotenv()
def main():
    
    knowledgehub = KnowledgeHubService()

    print()

    print("=" * 60)
    print("KnowledgeHub AI")
    print("Escribe 'salir' para terminar.")
    print("=" * 60)

    while True:

        question = input("\nPregunta: ")

        if question.lower() == "salir":
            break

        result = knowledgehub.ask(question)

        print("\nRespuesta\n")

        print(result["answer"])

        print("\nFuentes consultadas")

        for document in result["documents"]:

            print(
                f"- {document.metadata['filename']} "
                f"(Página {document.metadata['page'] + 1})"
            )


if __name__ == "__main__":
    main()