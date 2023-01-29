
def repeat(iters: int):
    """Функция, которая вернет декоратор."""
    def decorator_function(func):
        """Декоратор, который вернет обертку."""
        def wrapper(*args, **kwargs):
            """Обертка функции, которая вызовет оборачиваюмую функцию."""
            for _ in range(iters):
                func(*args, **kwargs)
        return wrapper
    return decorator_function


@repeat(3)
def hello_world(msg='Hello world!'):
    print(msg)


if __name__ == '__main__':
    hello_world('I love running!')
    print('*' * 30)
