__author__ = 'Magomedov Ramazan'
#Создать текстовый файл (не программно), построчно записать
#фамилии сотрудников и величину их окладов.
#Определить, кто из сотрудников имеет оклад менее 20 тыс.,
#вывести фамилии этих сотрудников. Выполнить подсчет средней
#величины дохода сотрудников.

from statistics import mean
with open("sal.txt", "r", encoding="utf-8") as my_file:
    salaries = []
    for line in my_file:
        worker, salary = line.split()
        salary = float(salary)
        if salary < 20_000:
            print(worker, " - низкий доход")
        salaries.append(salary)
    print("Средняя величина дохода всех сотрудников: ", mean(salaries))