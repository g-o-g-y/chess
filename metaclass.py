from functools import wraps


def debug(func):
    """Декоратор для указания вызываемой функции"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Переход к методу:", func.__qualname__)
        return func(*args, **kwargs)
    return wrapper


def debug_methods(cls):
    """Отладка методов класса"""
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))
    return cls


class DebugMeta(type):
    """metaclass передает созданный класс для получения требуемой
       функциональности при отладке (debug_methods)"""
    def __new__(cls, name, bases, dct):
        obj = super().__new__(cls, name, bases, dct)
        obj = debug_methods(obj)
        return obj
