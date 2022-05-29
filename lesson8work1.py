__author__ = 'Magomedov Ramazan'
"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных. """


class MyDate:
    _year = 0
    _month = 0
    _day = 0
    __months = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    is_leap = None

    def __init__(self, str_date: str):
        """
        принимает дату в виде строки формата «день-месяц-год».
        :param str_date:
        """

        self._build_date(str_date)
        if MyDate._is_ok_year(self._year):
            self.is_leap = MyDate.is_leap_year(self._year)
        else:
            raise ValueError('My date structure (year) is incorrect')
        if not MyDate.check_date(self._day, self._month, self._year):
            raise ValueError('The data for date is not allowed')

    @staticmethod
    def is_leap_year(year):
        """
        1. Если год делится на 4 без остатка, перейдите на шаг 2.
            В противном случае перейдите к выполнению действия 5.
        2. Если год делится на 100 без остатка, перейдите на шаг 3.
            В противном случае перейдите к выполнению действия 4.
        3. Если год делится на 400 без остатка, перейдите на шаг 4.
            В противном случае перейдите к выполнению действия 5.
        4. Год високосный (366 дней).
        5. Год не високосный год (365 дней).
        https://docs.microsoft.com/ru-ru/office/troubleshoot/excel/determine-a-leap-year
        :return:
        """
        if not year % 4:  # 1
            if not year % 100:  # 2
                if not year % 400:
                    return True
                else:
                    return False
            else:
                return True
        else:  # 5
            return False

    @classmethod
    def set_date(cls, str_date: str):
        """
        Извлекает число, месяц, год и возвращает объект с данными типа int
        :param str_date:
        :return:
        """
        return cls(str_date)

    @staticmethod
    def check_date(date, month, year, verbose=False):
        """
        Проверяет детально дату включая максимальную дату месяца с учетом високосных лет
        :param date:
        :param month:
        :param year:
        :param verbose:
        :return:
        """
        is_ok = False
        if verbose:
            print(f'{date} - {month} - {year}')
        if 1 <= month <= 12:
            is_ok = True
        elif verbose:
            print('the month is wrong number')
        if is_ok:
            is_ok = date <= MyDate.__months[month + 1]
            if not is_ok and verbose:
                print('the day is wrong number of month')
        if is_ok:
            is_ok = MyDate._is_ok_year(year)
            if not is_ok and verbose:
                print('the year is not belong to correct period')
        if is_ok and month == 2:
            is_ok = not MyDate.is_leap_year(year) and date <= 28
            if not is_ok and verbose:
                print('the day of Feb is wrong')
        if verbose:
            print(f' date is {"ok" if is_ok else "wrong"}')
        return is_ok

    @staticmethod
    def _is_ok_year(year):
        # мои правила проверки года
        return 1970 <= year <= 2060

    def _build_date(self, str_date):
        #  принимает дату в виде строки формата «день-месяц-год».
        self._day, self._month, self._year = tuple(map(int, str_date.split('-')))

    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year


if __name__ == '__main__':
    d1 = MyDate.check_date(13, 2, 1977, verbose=True)
    d2 = MyDate.check_date(13, 2, 1967, verbose=True)
    d3 = MyDate.check_date(30, 2, 1977, verbose=True)
    d4 = MyDate.check_date(29, 2, 2000, verbose=True)

    D1 = MyDate.set_date('13-02-1977')
    print(f'D1: {D1.day} {D1.month} {D1.year}')
    D2 = MyDate('13-02-1977')
    print(f'D2: {D2.day} {D2.month} {D2.year}')