__author__ = 'Magomedov Ramazan'
# Реализовать функцию my_func(), которая принимает три
# позиционных аргумента и возвращает сумму наибольших
# двух аргументов.
def my_func():
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    c = float(input("Введите число c: "))
    return a + b + c - min(a, b, c)

print("Сумма наибольших двух аргументов: ", my_func())