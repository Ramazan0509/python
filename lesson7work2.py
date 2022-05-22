__author__ = 'Magomedov Ramazan'
"""Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого 
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и 
H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 
0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода 
ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов 
проекта, проверить на практике работу декоратора @property. """
class Clothes:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        total_cloth = self.__dict__.get('cloth_coat') + other.__dict__.get('cloth_suit')
        return print(f'Общая длина ткани для обоих элементов равна {total_cloth.__round__(2)} м')

class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def get_cloth(self):
        cloth_coat = self.size / 6.5 + 0.5
        self.cloth_coat = cloth_coat
        return self.name, self.cloth_coat.__round__(2)

class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    def get_cloth(self):
        cloth_suit = 2 * self.height + 0.3
        self.cloth_suit = cloth_suit
        return self.name, self.cloth_suit.__round__(2)

coat = Coat('Coat', 10)
print(f'Длина ткани для {coat.get_cloth()[0]} это {coat.get_cloth()[1]} м')

suit = Suit('Suit', 1.8)
print(f'Длина ткани для {suit.get_cloth()[0]} это {suit.get_cloth()[1]} м')

coat + suit