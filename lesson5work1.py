__author__ = 'Magomedov Ramazan'
# Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

my_file = open("text.txt", "w", encoding="utf-8")
line = input("Введите текст \n")
my_file.writelines(line)
my_file.close()

my_file = open("text.txt", "r")
content = my_file.readlines()
print(content)
my_file.close()