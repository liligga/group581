def printer(func):
    print(func.__name__)
    def wrapper(*args, **kwargs):
        print(f"До вызова ф-ии {func.__name__}")
        result = func(*args, **kwargs)
        print(f"После вызова ф-ии {func.__name__}")
        return result

    return wrapper

@printer
def hello_world():
    print("Hello World!")

@printer
def add_numbers(number1, number2):
    return number1 + number2

hello_world()
print(add_numbers(1, 2))


def blahblah():
    print("blah blah blah")

blahblah = printer(blahblah)
blahblah()