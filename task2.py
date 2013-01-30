#!/usr/bin/python

from functools import *

def lazy_decorator(decorator):
    @wraps(decorator)
    def inner(function):
        @wraps(function)
        def outer(*args, **kwargs):
            return decorator(function)(*args, **kwargs)
        return outer
    return inner




