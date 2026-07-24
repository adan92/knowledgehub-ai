from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.chat import router as chat_router
from backend.routes.documents import router as documents_router
from backend.routes.health import router as health_router

app = FastAPI(
    title="KnowledgeHub API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # luego restringimos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    health_router,
    prefix="/health",
    tags=["Health"]
)

app.include_router(
    chat_router,
    prefix="/chat",
    tags=["Chat"]
)

app.include_router(
    documents_router,
    prefix="/documents",
    tags=["Documents"]
)