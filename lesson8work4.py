__author__ = 'Magomedov Ramazan'
"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники. """


class WarehouseEquipments:
    shelf = {}

    def __init__(self, shelf):
        self.shelf = shelf


class OfficeEquipment:
    inventory_number = 0
    dimensions = (0, 0)
    weight = 0
    place = (0, 0)
    is_network = False


class Printer(OfficeEquipment):
    letter_size = ''
    color = False


class CopyMachine(OfficeEquipment):
    auto_feeder = False


class Scanner(OfficeEquipment):
    is_pdf_ready = False