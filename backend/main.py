from src.worker import create_celery
from src.server import create_app


app = create_app()
celery = create_celery(app)