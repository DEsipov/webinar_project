
def one(func):
    def wrapper():
        print('one decorator')
        func()
    return wrapper


def two(func):
    def wrapper():
        print('two decorator')
        func()
    return wrapper


@one
@two
def hello_world():
    """Выполнение декораторов идет сверху вниз."""
    print('Hello world!')


if __name__ == '__main__':
    hello_world()
    print('*' * 30)
