
def decorator_function(func):
    def wrapper(*args, **kwargs):
        """Аргументы из wrapper идут в декорируемую функцию."""
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func(*args, **kwargs)
        print('Выходим из обёртки')
    return wrapper


@decorator_function
def hello_world(message='Hello world!', caps=False):
    """Декорируем функцию, используя синтаксический сахар."""
    res = message.upper() if caps else message
    print(res)


if __name__ == '__main__':
    hello_world()
    print('*' * 30)
    hello_world(message='Bye-Bye!', caps=True)
    print('*' * 30)
