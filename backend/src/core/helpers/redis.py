from redis import asyncio as redis

from src.core.config import config

redis_client = redis.from_url(url=f"redis://{config.REDIS_HOST}", decode_responses=True)
