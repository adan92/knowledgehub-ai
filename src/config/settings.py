from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_base_url: str = "http://localhost:8000"
    google_api_key: str = ""
    cohere_api_key: str = ""

    class Config:
        env_file = ".env"


settings = Settings()