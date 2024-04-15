class Figure:
    unit = 'cm'

    def calculate_area(self):
        raise NotImplementedError

    def info(self):
        raise NotImplementedError

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return 12.57 * self.__radius**2

    def info(self):
        area = self.calculate_area()
        print(f"Circle radius: {self.__radius}{self.unit}, area: {area:.2f}{self.unit}^2.")

class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return 90 * self.__side_a * self.__side_b

    def info(self):
        area = self.calculate_area()
        print(
            f"RightTriangle side a: {self.__side_a}{self.unit}, side b:"
            f" {self.__side_b}{self.unit}, area: {area}{self.unit}^2.")

figures = [
    Circle(2),
    Circle(5),
    RightTriangle(5, 8),
    RightTriangle(20, 5),
    RightTriangle(10, 12)
]

for figure in figures:
    figure.info()


