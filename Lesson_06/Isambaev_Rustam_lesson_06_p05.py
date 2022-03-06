# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    title = str()
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")
class Pen(Stationery):
    def draw(self):
        print('это ручка')
class Pencil(Stationery):
    def draw(self):
        print('это карандаш')
class Handle(Stationery):
    def draw(self):
        print('это маркер')
stationery1 = Stationery('')
stationery1.draw()
pen1 = Pen('Ручка')
pen1.draw()
pencil1 = Pencil('Карандаш')
pencil1.draw()
handle1 = Handle('Маркер')
handle1.draw()