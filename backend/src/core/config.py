import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    ENV: str
    DB_ENGINE: str = os.getenv("DB_ENGINE", None)
    DB_USERNAME: str = os.getenv("DB_USERNAME", None)
    DB_PASS: str = os.getenv("DB_PASS", None)
    DB_HOST: str = os.getenv("DB_HOST", None)
    DB_PORT: str = os.getenv("DB_PORT", None)
    DB_NAME: str = os.getenv("DB_NAME", None)

    REDIS_HOST: str = os.getenv("REDIS_HOST", None)

    CELERY_BACKEND_URL: str = os.getenv("CELERY_BACKEND_URL", None)
    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", None)

    model_config = SettingsConfigDict(env_file="../.env")

    @property
    def writer_db_url(self):
        return f"{self.DB_ENGINE}://{self.DB_USERNAME}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    @property
    def reader_db_url(self):
        return f"{self.DB_ENGINE}://{self.DB_USERNAME}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class ProductionConfig(Config):
    DEBUG: bool = False


class DevelopmentConfig(Config):
    DEBUG: bool = True


def get_config():
    print(os.getenv("DB_ENGINE", None))
    env = os.getenv("ENV", "test")
    config_type = {
        "test": DevelopmentConfig(),
        "prod": ProductionConfig(),
    }
    print(config_type["test"].DB_ENGINE)
    return config_type[env]


config: Config = get_config()
