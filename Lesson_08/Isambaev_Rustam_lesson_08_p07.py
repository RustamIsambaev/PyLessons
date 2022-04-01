class ComplexNum:
    def __init__(self, real, imagine):
        self.real = real
        self.imagine = imagine

    def __str__(self):
        return f"{self.real}{' + ' if self.imagine >= 0 else ' - '}" \
               f"{abs(self.imagine) if abs(self.imagine) != 1 else ''}i"

    def __add__(self, other):
        return ComplexNum(self.real + other.real, self.imagine + other.imgine)

    def __mul__(self, other):
        return ComplexNum(self.real * other.real - self.imagine * other.imagine, self.real * other.imagine
                          + other.real * self.imagine)


print(ComplexNum(1, 2) * ComplexNum(-11, 15))
