# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги
# асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.
class Road:

    def __init__(self, road_length: int, road_width: int):
        self._length = road_length
        self._width = road_width

    def asphalt_mass_count(self, asphalt_mass_pr_meter, road_height):
        return self._length * self._width * asphalt_mass_pr_meter * road_height


myroad = Road(5000, 20)

print(int(myroad.asphalt_mass_count(25, 5) / 1000))
