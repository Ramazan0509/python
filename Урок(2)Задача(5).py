__author__ = 'Magomedov Ramazan'
#Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
#У пользователя необходимо запрашивать новый элемент рейтинга.
#Если в рейтинге существуют элементы с одинаковыми значениями,
#то новый элемент с тем же значением должен разместиться после них.
my_list = [5, 4, 3, 2, 1]
print(f'"Рейтинг" - {my_list}')
digit = int(input("Введите число (0 - выход): "))
while digit != 0:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"Результат: - {my_list}")
    digit = int(input("Введите число (0 - выход): "))