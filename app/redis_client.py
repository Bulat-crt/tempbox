import os
from dotenv import load_dotenv
from redis import Redis
load_dotenv()

redis_url = os.getenv('REDIS_URL')

redis_client = Redis.from_url(redis_url, decode_responses=True)