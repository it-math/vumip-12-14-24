def print_hello(x):
    return f'Hello, {x}!'


if __name__ == '_main__':
    s = input('Введите имя: ')
    print(print_hello(s))