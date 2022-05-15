__author__ = 'Magomedov Ramazan'
# Напишите программу, открывающую файл на чтение
# и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_file = []
with open("numbers.txt", "r+", encoding="utf-8") as my_file:
      for i in my_file:
        i = i.split(" ", 1)
        new_file.append(dict[i[0]] + "  " + i[1])


with open("numbers_1.txt", "w", encoding="utf-8") as my_file_1:
    my_file_1.writelines(new_file)

with open("numbers_1.txt", "r", encoding="utf-8") as my_file_1:
    for line in my_file_1:
        print(line)