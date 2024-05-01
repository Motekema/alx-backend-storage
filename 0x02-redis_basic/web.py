#!/usr/bin/env python3
"""
Web Cache Module
"""
import requests
import redis
import time
from functools import wraps
from typing import Callable

def track_access(func: Callable) -> Callable:
    """
    Decorator to track the number of times a URL is accessed
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        """
        Wrapper function to track URL access and cache the result
        """
        # Increment access count for the URL
        redis_client = redis.Redis()
        redis_client.incr(f"count:{url}")
        
        # Cache the result with an expiration time of 10 seconds
        cached_content = redis_client.get(url)
        if cached_content:
            return cached_content.decode('utf-8')
        else:
            content = func(url)
            redis_client.setex(url, 10, content)
            return content
    return wrapper

@track_access
def get_page(url: str) -> str:
    """
    Retrieve HTML content of a URL
    """
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.google.co.uk"
    print(get_page(url))
