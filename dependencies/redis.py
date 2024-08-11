import redis
from core.settings import settings


class RedisClient:
    def __init__(self):
        self.host = settings.redis_host
        self.port = settings.redis_port
        self._client = redis.Redis(host=self.host, port=self.port)

        self._expire_seconds = 180

    def get_client(self):
        return self._client

    def set(self, key: str, value: str, expire_seconds: int = None):
        ex = expire_seconds or self._expire_seconds
        self._client.set(key, value, ex=ex)

    def get(self, key: str):
        return self._client.get(key)

    def delete(self, key: str):
        self._client.delete(key)

    def search_pattern(self, pattern: str):
        return self._client.keys(pattern=f"{pattern}*")

