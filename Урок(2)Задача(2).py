element_count = int(input("Введите количество элементов списка: "))
my_list = []
i = 0
element = 0
while i < element_count:
    my_list.append(input("Введите значение списка: "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[element], my_list[element + 1] = my_list [element + 1], my_list[element]
        element += 2
print(my_list)