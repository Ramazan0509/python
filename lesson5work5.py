__author__ = 'Magomedov Ramazan'

# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
with open("sum_numbers.txt", "w+", encoding="utf-8") as my_file:
    num = ["1 4 7 3"]
    my_file.writelines(num)


with open("sum_numbers.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        print(line)

    sum_num = [sum(map(int, s.split())) for s in num]
    print(sum_num)