from functools import wraps
from typing import Callable, Any

def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in results:
            print("Getting from cache")
            return results[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        results[key] = result

        return result

    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b + c) % (a ** c)


@cache
def long_time_func_2(numbers_tuple: tuple, power: int) -> list:
    return [number ** power for number in numbers_tuple]


long_time_func(2, 2, 3)
long_time_func(2, 2, 3)

long_time_func_2((5, 6, 7), 5)
long_time_func_2((5, 6, 7), 5)

long_time_func(1, 2, 3)
long_time_func(5, 6, 7)

long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
