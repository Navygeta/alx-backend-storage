#!/usr/bin/env python3
"""
Caching request module
"""
import redis
import requests
from functools import wraps
from typing import Callable


def track_get_page(fn: Callable) -> Callable:
    """Decorator to track and cache HTTP GET requests.

    Args:
        fn (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    """
    @wraps(fn)
    def wrapper(url: str) -> str:
        """Wrapper function to cache and track HTTP GET requests.

        Args:
            url (str): The URL to request data from.

        Returns:
            str: The response content.
        """
        client = redis.Redis()
        client.incr(f'count:{url}')
        cached_page = client.get(f'{url}')
        if cached_page:
            return cached_page.decode('utf-8')
        response = fn(url)
        client.set(f'{url}', response, 10)
        return response
    return wrapper


@track_get_page
def get_page(url: str) -> str:
    """Makes an HTTP GET request to the specified URL.

    Args:
        url (str): The URL to request data from.

    Returns:
        str: The response content.
    """
    response = requests.get(url)
    return response.text
