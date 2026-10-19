import os
from dotenv import load_dotenv
from redis import Redis
load_dotenv()

redis_url = os.getenv('REDIS_URL')

connect = Redis(host='localhost', port=6369, db=0, decode_responses=True)