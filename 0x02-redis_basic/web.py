#!/usr/bin/env python3
'''A module providing tools for request caching and tracking.'''
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
'''The Redis instance used for caching and tracking requests.'''


def data_cacher(method: Callable) -> Callable:
    '''Decorator to cache the output of data fetched from a URL.'''
    @wraps(method)
    def invoker(url) -> str:
        '''
            Wrapper function for caching the output of data fetched
            from a URL.
        '''
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''
        Fetches the content of a URL, caches the response,
       and tracks the request.
    '''
    return requests.get(url).text
