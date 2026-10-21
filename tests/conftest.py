import pytest
from redis import Redis
from fastapi.testclient import TestClient
from app.services import note_service
from main import app
from app.config import test_url


@pytest.fixture(autouse=True)
def redis_test(monkeypatch):
    if not test_url:
        raise RuntimeError("TEST_REDIS_URL is not set")

    test_redis = Redis.from_url(
        test_url,
        decode_responses=True
    )

    test_redis.flushdb()
    monkeypatch.setattr(note_service, "redis_client", test_redis)

    try:
        yield
    finally:
        test_redis.flushdb()
        test_redis.close()


@pytest.fixture
def client(redis_test):
    with TestClient(app) as test_client:
        yield test_client
