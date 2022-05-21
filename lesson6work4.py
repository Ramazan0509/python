__author__ = 'Magomedov Ramazan'
"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат. """


class Car:
    def __init__(self, speed: int, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Вперед')

    def stop(self):
        print('Стоп')

    def turn(self, side):
        print(side)

    def show_speed(self):
        print(f'Скорость : {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"Превышена скорость на {self.speed - 60}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"Превышена скорость на {self.speed - 40}")


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)
        self.is_police = True


if __name__ == '__main__':

    for car in [TownCar(55, 'красная', 'Toyota'), SportCar(80, 'белая', 'Nissan'), WorkCar(50, 'коричневая', 'Ford'),
                PoliceCar(90, 'синяя', 'Ford')]:
        print('---')
        print(car.name, car.color, car.speed)
        car.show_speed()
        car.go()
        car.turn('налево')
        car.stop()
