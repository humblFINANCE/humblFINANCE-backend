import os

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DB_ENGINE: str | None = os.getenv("DB_ENGINE", None)
    DB_USERNAME: str | None = os.getenv("DB_USERNAME", None)
    DB_PASS: str | None = os.getenv("DB_PASS", None)
    DB_HOST: str | None = os.getenv("DB_HOST", None)
    DB_PORT: str | None = os.getenv("DB_PORT", None)
    DB_NAME: str | None = os.getenv("DB_NAME", None)

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "humblFINANCE FastAPI Backend"


class ProductionConfig(Config):
    DEBUG: bool = False


class DevelopmentConfig(Config):
    DEBUG: bool = True