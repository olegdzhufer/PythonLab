"""Modul that containing logged decorator"""
import logging


def logged(exception, mode):
    """logging"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as ex:
                if mode == 'console':
                    logging.error(f'Exception: {ex}', exc_info=True)
                elif mode == 'file.txt':
                    logging.basicConfig(filename='file.txt', level=logging.ERROR, filemode='w')
                    logging.error(f'Exception: {ex}', exc_info=True)

        return wrapper

    return decorator
