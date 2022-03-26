from log_decorator import log_decorator_factory

LOG_FILE = 'log.txt'


@log_decorator_factory(LOG_FILE)
def my_function(name: str):
    print(f'Hello, {name}!')


if __name__ == '__main__':
    my_function('Иван')

