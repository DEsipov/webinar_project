
def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper


@decorator_function
def hello_world():
    """Декорируем функцию, используя синтаксический сахар."""
    print('Hello world!')


if __name__ == '__main__':
    hello_world()
    print('*' * 30)
    # Обратите внимание, что hello_world не то, чем кажется.
    print(hello_world)
