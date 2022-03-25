# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.
class Car:
    speed = int()
    color = str()
    name = str()
    is_police = bool()

    def __init__(self, name, color):
        self.name = name
        self.speed = 0
        self.color = color
        self.is_police = False

    def go(self, speed):
        if speed > self.speed > 0:
            print(f'автомобиль {self.name} увеличил свою скорость движения')
        elif self.speed > speed > 0:
            print(f'автомобиль {self.name} уменьшил свою скорость движения')
        elif self.speed == 0:
            print(f'автомобиль {self.name} начал движение')
        self.speed = speed

    def stop(self):
        self.speed = 0
        print(f'автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'автомобиль {self.name} повернул {direction}')

    def show_speed(self):
        print(f'скорость автомобиля {self.name}: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            print(f'Скорость автомобиля {self.name} превышает 60 км/ч!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40:
            print(f'Скорость автомобиля {self.name} превышает 40 км/ч!')


class PoliceCar(Car):
    def __init__(self, name, color):
        Car.__init__(self, name, color)
        self.is_police = True
    def onduty(self):
        print(f'автомобиль ДПС {self.name} производит патрулирование')


towncar1 = TownCar('mazda', 'black')
print(f'Создан объект {str(type(towncar1))[17:-2]} с атрибутами\nмарка: {towncar1.name}\nскорость: {towncar1.speed}\nцвет: {towncar1.color}\nполицейский автомобиль: {towncar1.is_police}')
towncar1.go(70)
towncar1.show_speed()
patrul1 = PoliceCar('opel','white with two blue stripes')
print(f'Создан объект {str(type(patrul1))[17:-2]} с атрибутами\nмарка: {patrul1.name}\nскорость: {patrul1.speed}\nцвет: {patrul1.color}\nполицейский автомобиль: {patrul1.is_police}')
patrul1.onduty()
towncar1.go(10)
towncar1.show_speed()
towncar1.turn('налево')
towncar1.stop()
towncar1.show_speed()
workcar1 = WorkCar('kamaz', 'orange')
print(f'Создан объект {str(type(workcar1))[17:-2]} с атрибутами\nмарка: {workcar1.name}\nскорость: {workcar1.speed}\nцвет: {workcar1.color}\nполицейский автомобиль: {workcar1.is_police}')
workcar1.go(50)
workcar1.show_speed()
workcar1.go(45)
workcar1.show_speed()
workcar1.go(40)
workcar1.show_speed()
sportcar1 = SportCar('lamborgini', 'yellow')
print(f'Создан объект {str(type(sportcar1))[17:-2]} с атрибутами\nмарка: {sportcar1.name}\nскорость: {sportcar1.speed}\nцвет: {sportcar1.color}\nполицейский автомобиль: {sportcar1.is_police}')
sportcar1.go(100)
sportcar1.show_speed()
sportcar1.go(200)
sportcar1.show_speed()
sportcar1.go(120)
sportcar1.show_speed()
sportcar1.turn('направо')
sportcar1.turn('налево')
sportcar1.stop()
