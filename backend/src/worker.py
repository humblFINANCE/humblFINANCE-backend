from celery import Celery
from fastapi import FastAPI
from src.core.config import config


def create_celery(app: FastAPI) -> Celery:
    celery_app = Celery(
        app.title,
        backend=config.CELERY_BACKEND_URL,
        broker=config.CELERY_BROKER_URL,
    )
    celery_app.config_from_object("src.core.config:config", namespace="CELERY")
    celery_app.autodiscover_tasks()

    celery_app.conf.update(task_track_started=True)

    return app