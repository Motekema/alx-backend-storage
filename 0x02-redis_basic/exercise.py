#!/usr/bin/env python3
"""
Cache Module
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class for storing data in Redis
    """
    def __init__(self) -> None:
        """
        Initialize Cache instance with Redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis and return the generated key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

if __name__ == "__main__":
    pass
