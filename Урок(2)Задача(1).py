my_list = [None, 0, 'Один', True, 0.1]


def my_type(element):
    for element in range(len(my_list)):
        print(type(my_list[element]))
    return


my_type(my_list)