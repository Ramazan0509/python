__author__ = 'Magomedov Ramazan'
# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

from statistics import mean
with open("bill.txt", "r", encoding="utf-8") as my_file:
    salaries = []
    for line in my_file:
        worker, salary = line.split()
        salary = float(salary)
        if salary < 20_000:
            print(worker, " - низкий доход")
        salaries.append(salary)
    print("Средняя величина дохода всех сотрудников: ", mean(salaries))