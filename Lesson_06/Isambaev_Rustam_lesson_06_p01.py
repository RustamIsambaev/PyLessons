# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.
from random import choice
from time import sleep
from sys import exit


class TrafficLight:
    """Это класс "светофор\""""
    __color = str()

    def __init__(self):
        self.__color = 'зеленый'

    def __del__(self):
        print('светофор неисправен')

    # в методе предусмотрена проверка порядка смены режимов светофора
    def running(self, nextcolor):
        """Это метод "запуск" класса "светофор\""""
        nextcolorindex = color_order.index(self.__color) + 1 if color_order.index(self.__color) < 2 else 0
        self.__color = nextcolor
        print(self.__color)
        if nextcolor != color_order[nextcolorindex]:
            exit()  # завершение скрипта в случае нарушения порядка смены режима
        sleep(colors[self.__color])


# интервалы смены режимов
colors = {'красный': 7, 'желтый': 2, 'зеленый': 5}

# порядок режимов
color_order = tuple(colors.keys())

# создаем объект
TrafficLight1 = TrafficLight()

# прогон режимов по порядку
for color in color_order:
    TrafficLight1.running(color)

# проверка порядка режима
while True:
    TrafficLight1.running(choice(color_order))  # установка случайного режима
