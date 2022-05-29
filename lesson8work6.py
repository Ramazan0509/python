__author__ = 'Magomedov Ramazan'
"""6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. Подсказка:
постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
import datetime


class WarehouseEquipments:
    """ Класс реализации склада
    """
    shelf = {}  # склад
    in_work = {}  # выдано
    log = []  # журнал
    __current_num = 1000

    def __init__(self, shelf=None):
        if shelf is None:
            shelf = {}
        self.take_storage_equipments(shelf)

    def take_storage_equipments(self, equipments):
        """Принять на хранение списком
        :param equipments:
        :return:
        """
        for machine in equipments:
            self.take_storage(machine)

    def take_storage(self, equipment):
        """Принять на хранение
        :param equipment:
        :return:
        """
        if isinstance(equipment, OfficeEquipment):
            for _ in range(equipment.number):
                self.__current_num += 1
                equipment.inventory_number = self.__current_num
                self.shelf[self.__current_num] = equipment
                self.log_operation('Прием', equipment)

    def find_by_inventory(self, number):
        """Найти по Инв
        :param number:
        :return:
        """
        return self.shelf[number]

    def move_in_work(self, inventory, division):
        """Выдать в подразделение
        :param inventory:
        :param division:
        :return:
        """
        equipment = self.shelf[inventory]
        self.in_work[inventory] = (equipment, division)
        del (self.shelf[inventory])
        self.log_operation('Выдано', equipment, division=division)

    def move_in_shelf(self, inventory):
        """Вернуть на склад
        :param inventory:
        :return:
        """
        equipment, _ = self.in_work[inventory]
        self.shelf[inventory] = equipment
        del (self.in_work[inventory])
        self.log_operation('Возврат', equipment)

    def print_shelf(self):
        for inventory, equipment in self.shelf.items():
            print(equipment)

    def print_in_work(self):
        for inventory, (equipment, division) in self.in_work.items():
            print(f'{equipment} {division}')

    def log_operation(self, operation, equipment, division=''):
        """Логирование операции
        :param operation:
        :param equipment:
        :param division:
        :return:
        """
        self.log.append(f' {datetime.datetime.now().isoformat()} - {operation} : {equipment} {division}')

    def log_print(self):
        for line in self.log:
            print(line)


class OfficeEquipment:
    brand = ''
    model = ''
    inventory_number = 0
    dimensions = (0, 0)
    weight = 0
    place = (0, 0)
    is_network = False
    number = 0
    type = ''

    def __init__(self, brand, model, number=1):
        self.brand = brand
        self.model = model
        self.number = number

    def __str__(self):
        return f'{self.inventory_number} {self.type} {self.brand} {self.model}'


class Printer(OfficeEquipment):
    type = 'Принтер'
    letter_size = ''
    color = False


class CopyMachine(OfficeEquipment):
    type = 'Копир'
    auto_feeder = False


class Scanner(OfficeEquipment):
    type = 'Сканер'
    is_pdf_ready = False


class MenuController:
    __WH = None

    def __init__(self, wh: WarehouseEquipments):
        self.__WH = wh
        self.builder = [None, Printer, Scanner, CopyMachine]  # Создать Об по типу
        # меню операций
        self.action = [lambda: True,
                       self.refresh, self.add_equipment, self.move_in_work, self.move_shelf, self.log_print]

    def run(self):
        """ Главный цикл приложения
        :return:
        """
        while True:
            self.action[1]()  # обновить экран
            if self.action[self.print_menu()]():
                break

    def log_print(self):
        print('=== Журнал операций')
        self.__WH.log_print()

    def print_menu(self):
        print('1 - Обновить | 2 - Добавить | 3 - Выдать | 4 - Принять')
        print('-----------')
        print('5 - Журнал операций')
        print('0 - Выход')
        return self.input_int('? :')

    def refresh(self):
        print('=== Cocтояние склада')
        self.__WH.print_shelf()
        print(f'=== Итого: {len(self.__WH.shelf)}')
        print('')
        print('=== Выдано')
        self.__WH.print_in_work()
        print(f'=== Итого: {len(self.__WH.in_work)}')
        print('')
        return False

    def add_equipment(self):
        print('=== Введите оборудование')
        type_eq = input('Модель (1-Принтер, 2-Сканер, 3-Копир) :')
        brand = input('Бренд :')
        model = input('Модель:')
        number = self.input_int('Количество :')
        eq = self.builder[int(type_eq)](brand, model, int(number))
        self.__WH.take_storage(eq)
        return False

    def move_in_work(self):
        inventory = self.input_int('ВВедите инв N :')
        division = input('Введите отдел :')
        self.__WH.move_in_work(int(inventory), division)
        return False

    def move_shelf(self):
        inventory = input('ВВедите инв N :')
        self.__WH.move_in_shelf(int(inventory))
        return False

    @staticmethod
    def input_int(text):
        while True:
            buf = input(text)
            if buf.isdigit():
                return int(buf)


class SideKick:
    """
    Наполнение склада
    """

    @staticmethod
    def full_wh(wh: WarehouseEquipments):
        sc_1 = Scanner('Canon', 'CanoScan LiDE 400')
        sc_2 = Scanner('Epson', 'Perfection V19')
        sc_3 = Scanner('Panasonic', 'KV-SL1066')
        pr_1 = Printer('Xerox', 'Phaser 3020BI')
        pr_2 = Printer('HP', 'LaserJet Pro M15w')
        pr_3 = Printer('Brother', 'HL-L2340DWR')
        cp_1 = CopyMachine('Xerox', 'B1022')
        cp_2 = CopyMachine('Xerox', 'B215')
        cp_3 = CopyMachine('Konica-Minolta', 'A0XY026')
        wh.take_storage_equipments([sc_1, sc_2, sc_3, pr_1, pr_2, pr_3, cp_1, cp_3, cp_2])
        wh.move_in_work(1005, 'Secretary')
        wh.move_in_work(1006, 'Secretary')
        wh.move_in_work(1007, 'R&D')
        wh.move_in_shelf(1005)
        wh.move_in_shelf(1006)


if __name__ == '__main__':
    wh1 = WarehouseEquipments()
    SideKick.full_wh(wh1)
    MenuController(wh1).run()