__author__ = 'Magomedov Ramazan'
# Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

my_file = open("text_file.txt", "r", encoding="utf-8")
content = my_file.readline()
s = 0
for i in content.split('(')[:-1]:
            r = int(i.rsplit(' ', 1)[1])
            s += r

content_1 = my_file.readline()
s_1 = 0
for i in content_1.split('(')[:-1]:
            r = int(i.rsplit(' ', 1)[1])
            s_1 += r

content_2 = my_file.readline()
s_2 = 0
for i in content_2.split('(')[:-1]:
            r = int(i.rsplit(' ', 1)[1])
            s_2 += r
print(f"Информатика: {s}, Физика: {s_1}, Физкультура: {s_2}")
my_file.close()