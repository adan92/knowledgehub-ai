from fastapi import APIRouter

from backend.schemas.chat import (
    ChatRequest,
    ChatResponse
)

from core.services.knowledgehub_service import (
    KnowledgeHubService
)

router = APIRouter()

service = KnowledgeHubService()


@router.post(
    "",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    result = service.ask(
        request.question
    )

    return ChatResponse(
        answer=result['answer'],
        sources=result['sources']
    )
