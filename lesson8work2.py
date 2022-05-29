__author__ = 'Magomedov Ramazan'
"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой. """


class MyZeroDivisionError(Exception):
    def __init__(self, message='Ошибка: Делитель = 0'):
        self.message = message

    def __str__(self):
        return self.message


if __name__ == '__main__':
    while True:
        buf = input('Введите 1 число :')
        if buf == '':
            break
        d1 = int(buf)
        d2 = int(input('Введите 2 число :'))
        try:
            if d2 == 0:
                raise MyZeroDivisionError('Ошибка: Делитель = 0')
            print(d1 / d2)
        except MyZeroDivisionError as e:
            print(e)