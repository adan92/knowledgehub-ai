from dataclasses import dataclass

import requests

from config.settings import settings


@dataclass(slots=True)
class ChatResponse:
    success: bool
    answer: str | None = None
    sources: list | None = None
    message: str | None = None


class ChatClient:
    def __init__(self):
        self.base_url = (
            f"{settings.api_base_url}/chat"
        )

    def ask(self, question: str):
        try:
            response = requests.post(
                self.base_url,
                json={
                    "question": question
                },
                timeout=180
            )

            if response.status_code == 429:
                return ChatResponse(
                    success=False,
                    message=(
                        "En este momento el modelo alcanzó su límite de uso. "
                        "Por favor intenta nuevamente en unos minutos."
                    )
                )

            response.raise_for_status()
            data = response.json()
            return ChatResponse(
                success=True,
                answer=data["answer"],
                sources=data["sources"]
            )

        except requests.Timeout:

            return ChatResponse(
                success=False,
                message="El servidor tardó demasiado tiempo en responder."
            )

        except requests.ConnectionError:
            return ChatResponse(
                success=False,
                message="No fue posible comunicarse con el servidor."
            )
        except requests.HTTPError:
            return ChatResponse(
                success=False,
                message="Ocurrió un error al procesar la solicitud."
            )
        except requests.RequestException:
            return ChatResponse(
                success=False,
                message="Ocurrió un error inesperado."
            )
