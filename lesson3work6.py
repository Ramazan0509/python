__author__ = 'Magomedov Ramazan'
#  Реализовать функцию int_func(), принимающую слова
#  из маленьких латинских букв и возвращающую их же,
#  но с прописной первой буквой.
#  Например, print(int_func(‘text’)) -> Text.
a = input("Введите слова из маленьких латинских букв: ")
def capitalize(str):
    str = str.title()
    return str
print(capitalize(a))