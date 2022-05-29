__author__ = 'Magomedov Ramazan'
"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата. """


class Complex:
    def __init__(self, re=0, im=0):
        self.Re = re
        self.Im = im
        self.I1 = 'j'  # в Python

    def __str__(self):
        # реализовано идентично complex
        if self.Re != 0:
            buf = f'({self.Re}{self.Im:+}{self.I1})'
        else:
            buf = f'{self.Im:-}{self.I1}'
        return buf

    def __add__(self, other):
        return Complex(self.Re + other.Re, self.Im + other.Im)

    def __sub__(self, other):
        return Complex(self.Re - other.Re, self.Im - other.Im)

    def __mul__(self, other):
        #  (a + bi) · (c + di) = (ac – bd) + (ad + bc)i
        re = self.Re * other.Re - self.Im * other.Im
        im = self.Re * other.Im + self.Im * other.Re
        return Complex(re, im)


if __name__ == '__main__':
    a = Complex(1, 3)
    a1 = complex(1, 3)
    print(a, a1)
    assert str(a) == str(a1), 'Не равно представление'
    print(Complex(0), Complex(0, 1), Complex(0, -1))
    assert str(Complex(0)) == str(complex(0)), 'Не равно представление'
    assert str(Complex(0, 1)) == str(complex(0, 1)), 'Не равно представление'
    assert str(Complex(0, -1)) == str(complex(0, -1)), 'Не равно представление'
    b = Complex(4, -5)
    b1 = complex(4, -5)
    assert str(b) == str(b1), 'Не равно представление отрицательных чисел'
    print(a, b, a1, b1)
    print(a + b, a1 + b1)
    assert str(a + b) == str(a1 + b1), 'Не равен результат сложения'
    print(a - b, a1 - b1)
    assert str(a - b) == str(a1 - b1), 'Не равен результат вычитания'
    print(a * b, a1 * b1)
    assert str(a * b) == str(a1 * b1), 'Не равен результат умножения'