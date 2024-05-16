#!/usr/bin/env python3
'''Module for interacting with Redis NoSQL data storage.'''
import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


def count_calls(method: Callable) -> Callable:
    '''Decorator to count method calls in a Cache instance.'''
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        '''Increment call count and invoke the method.'''
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


def call_history(method: Callable) -> Callable:
    '''Decorator to track method call history in a Cache instance.'''
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        '''Store input and output details before invoking the method.'''
        in_key = f"{method.__qualname__}:inputs"
        out_key = f"{method.__qualname__}:outputs"
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        return output
    return invoker


def replay(fn: Callable) -> None:
    '''Display call history of a Cache method.'''
    if not (fn and hasattr(fn, '__self__')):
        return
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return
    method_name = fn.__qualname__
    in_key = f"{method_name}:inputs"
    out_key = f"{method_name}:outputs"
    call_count = int(redis_store.get(method_name) or 0)
    print(f"{method_name} was called {call_count} times:")
    inputs = redis_store.lrange(in_key, 0, -1)
    outputs = redis_store.lrange(out_key, 0, -1)
    for inp, out in zip(inputs, outputs):
        print(f"{method_name}(*{inp.decode('utf-8')}) -> {out}")


class Cache:
    '''Object for managing data in Redis.'''
    def __init__(self) -> None:
        '''Initialize a Cache instance.'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Store data in Redis and return the generated key.'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        '''Retrieve data from Redis using the provided key.'''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        '''Retrieve a string value from Redis using the provided key.'''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''Retrieve an integer value from Redis using the provided key.'''
        return self.get(key, lambda x: int(x))
