import logging


def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == 'console':
                    logging.error(f'Exception: {e}')
                elif mode == 'file.txt':
                    logging.basicConfig(filename='file.txt', level=logging.ERROR)
                    logging.error(f'Exception: {e}')

        return wrapper

    return decorator
