__author__ = 'Magomedov Ramazan'
#Реализовать базовый класс Worker (работник).
#определить атрибуты: name, surname, position (должность), income (доход);
#последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
#элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
#создать класс Position (должность) на базе класса Worker;
#в классе Position реализовать методы получения полного имени сотрудника
#(get_full_name) и дохода с учётом премии (get_total_income);
#проверить работу примера на реальных данных: создать экземпляры класса
#Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
class Worker:

    def __init__(self, name='Иван', surname='Иванов', position='Админ', wage=100, bonus=20):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"Я {self.name} {self.surname} {self._income}")

    def get_total_income(self):
        print(f"Мой доход с учетом премии {sum(self._income.values())} руб. на позиции {self.position}")


ivan = Position("Иван", "Иванов", "Админ", 20000, 10000)
ivan.get_full_name()
ivan.get_total_income()