
def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper


def hello_world():
    """Диетический декоратор."""
    print('Hello world!')


hello_world = decorator_function(hello_world)


if __name__ == '__main__':
    hello_world()
    print('*' * 30)
