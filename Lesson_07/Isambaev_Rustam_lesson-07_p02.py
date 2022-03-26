from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def material_costs(self):
        pass

class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def material_costs(self):
        return round(self.size / 6.5 + 0.5, 2)

class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def material_costs(self):
        return round(2 * self.height + 0.3, 2)


my_coat = Coat(5)
print(f'расход ткани на пальто: {my_coat.material_costs}')
my_suit = Suit(1.831)
print(f'расход ткани на костюм: {my_suit.material_costs}')
print(f'общийй расход ткани: {my_coat.material_costs + my_suit.material_costs}')
