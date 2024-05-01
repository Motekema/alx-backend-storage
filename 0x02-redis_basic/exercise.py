#!/usr/bin/env python3
"""
Cache Module
"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """
    Cache class for storing and retrieving data in Redis
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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis using the provided key
        Optionally apply conversion function to the retrieved data
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, bytes, None]:
        """
        Retrieve data from Redis as string
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve data from Redis as integer
        """
        return self.get(key, fn=int)

if __name__ == "__main__":
    pass
