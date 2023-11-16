# Напишите функцию f, которая на вход принимает два числа a и b,
# и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.
from random import randint
def degree(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    return a * degree(a, b - 1)
num1 = randint(1, 4)
num2 = randint(2, 5)
print(num1, num2)
print(degree(num1, num2))