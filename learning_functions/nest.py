def two_numbers(a, b):
    def add():
        return a + b
    def sub():
        return a - b
    def multiply():
        return a * b
    def divide():
        return a / b
    return {'add': add(), 'sub': sub(), 'multiply': multiply(), 'divide': divide(),}


func = two_numbers(1,2)
print(func)