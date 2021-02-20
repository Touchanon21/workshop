
# EX1
def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))

print(f"{number1} + {number2} = {(add(number1,number2))}")
print(f"{number1} - {number2} = {(subtract(number1,number2))}")
print(f"{number1} * {number2} = {(multiply(number1,number2))}")
print(f"{number1} / {number2} = {(divide(number1,number2))}")
