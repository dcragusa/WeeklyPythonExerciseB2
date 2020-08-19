import time
from functools import wraps


class TooSoonError(Exception):
    pass


def once_per_minute(func):

    started = None

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal started
        elapsed = None if started is None else time.time() - started
        if elapsed is None or elapsed > 60:
            started = time.time()
            return func(*args, **kwargs)
        else:
            raise TooSoonError(f'Wait another {60 - elapsed} seconds')

    return wrapper
