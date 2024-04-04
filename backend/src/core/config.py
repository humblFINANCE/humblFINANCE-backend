import os

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DB_ENGINE = os.getenv("DB_ENGINE", None)
    DB_USERNAME = os.getenv("DB_USERNAME", None)
    DB_PASS = os.getenv("DB_PASS", None)
    DB_HOST = os.getenv("DB_HOST", None)
    DB_PORT = os.getenv("DB_PORT", None)
    DB_NAME = os.getenv("DB_NAME", None)


class ProductionConfig(Config):
    DEBUG: bool = False


class DevelopmentConfig(Config):
    DEBUG: bool = True
