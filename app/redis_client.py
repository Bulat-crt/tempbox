from app.config import redis_url
from redis import Redis

redis_client = Redis.from_url(redis_url, decode_responses=True)