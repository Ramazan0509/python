__author__ = 'Magomedov Ramazan'
"""5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь. """


class WarehouseEquipments:
    shelf = {}
    in_work = {}
    __current_num = 1000

    def __init__(self, shelf=None):
        self.take_storage_equipments(shelf)

    def take_storage_equipments(self, equipments):
        for machine in equipments:
            self.take_storage(machine)

    def take_storage(self, equipment):
        if isinstance(equipment, OfficeEquipment):
            for _ in range(equipment.number):
                self.__current_num += 1
                equipment.inventory_number = self.__current_num
                self.shelf[self.__current_num] = equipment

    def find_by_inventory(self, number):
        return self.shelf[number]

    def move_in_work(self, inventory, division):
        self.in_work[inventory] = (self.shelf[inventory], division)
        del (self.shelf[inventory])

    def move_in_shelf(self, inventory):
        self.shelf[inventory], _ = self.in_work[inventory]
        del (self.in_work[inventory])

    def print_shelf(self):
        for inventory, equipment in self.shelf.items():
            print(f'{inventory} {equipment.type} {equipment.brand} {equipment.model}')

    def print_in_work(self):
        for inventory, (equipment, division) in self.in_work.items():
            print(f'{inventory} {equipment.type} {equipment.brand} {equipment.model}  {division}')


class OfficeEquipment:
    brand = ''
    model = ''
    inventory_number = 0
    dimensions = (0, 0)
    weight = 0
    place = (0, 0)
    is_network = False
    number = 0

    def __init__(self, brand, model, number=1):
        self.brand = brand
        self.model = model
        self.number = number


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


if __name__ == '__main__':
    sc_1 = Scanner('Canon', 'CanoScan LiDE 400')
    sc_2 = Scanner('Epson', 'Perfection V19')
    sc_3 = Scanner('Panasonic', 'KV-SL1066')
    pr_1 = Printer('Xerox', 'Phaser 3020BI')
    pr_2 = Printer('HP', 'LaserJet Pro M15w')
    pr_3 = Printer('Brother', 'HL-L2340DWR')
    cp_1 = CopyMachine('Xerox', 'B1022')
    cp_2 = CopyMachine('Xerox', 'B215')
    cp_3 = CopyMachine('Konica-Minolta', 'A0XY026')
    wh1 = WarehouseEquipments([sc_1, sc_2, sc_3, pr_1, pr_2, pr_3])
    print('Склад создан')
    wh1.print_shelf()
    print('Добавлено оборудование')
    wh1.take_storage_equipments([cp_1, cp_2, cp_3])
    wh1.print_shelf()
    print('Выдано оборудование')
    wh1.move_in_work(1005, 'Secretary')
    wh1.move_in_work(1006, 'Secretary')
    wh1.move_in_work(1007, 'R&D')
    wh1.print_in_work()
    print('Возвращено оборудование')
    wh1.move_in_shelf(1005)
    wh1.move_in_shelf(1006)
    print('Склад')
    wh1.print_shelf()
    print('Выдано')
    wh1.print_in_work()