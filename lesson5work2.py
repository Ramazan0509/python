__author__ = 'Magomedov Ramazan'
# Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
my_file = open("doc.txt", "r")
content = my_file.readlines()
print(content)
print(f"Количество строк в файле - {len(content)}")
my_file.close()
my_file = open("doc.txt", "r")
content = my_file.readline()
content = content.split()
print(f"Общее количество слов 1-й строки - {len(content)}")
content = my_file.readline()
content = content.split()
print(f"Общее количество слов 2-й строки - {len(content)}")
my_file.close()