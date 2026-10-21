import os
from dotenv import load_dotenv

load_dotenv()

redis_url = os.getenv('REDIS_URL')

test_url = os.getenv('TEST_REDIS_URL')