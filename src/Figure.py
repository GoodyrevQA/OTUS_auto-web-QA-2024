from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Should be a Figure")
        return self.get_area + other_figure.get_area


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        if not isinstance(side_a, int | float) or not isinstance(side_b, int | float):
            raise ValueError("Rectangle sides can only be numbers")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Rectangle sides can't be less than 0")
        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2


class Square(Rectangle):
    def __init__(self, side_a):
        if not isinstance(side_a, int | float):
            raise ValueError("Square sides can only be numbers")
        if side_a <= 0:
            raise ValueError("Square sides can't be less than 0")
        super().__init__(side_a, side_a)
        # self.side_b = None


class Circle(Figure):
    def __init__(self, radius):
        if not isinstance(radius, int | float):
            raise ValueError("Circle radius can only be a number")
        if radius <= 0:
            raise ValueError("Circle radius can't be less than 0")
        self.radius = radius

    @property
    def get_area(self):
        return pi * self.radius**2

    @property
    def get_perimeter(self):
        return 2 * pi * self.radius


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if (
            not isinstance(side_a, int | float)
            or not isinstance(side_b, int | float)
            or not isinstance(side_c, int | float)
        ):
            raise ValueError("Triangle sides can only be numbers")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Triangle sides can't be less than 0")
        if (
            side_a + side_b <= side_c
            or side_a + side_c <= side_b
            or side_b + side_c <= side_a
        ):
            raise ValueError("A triangle with such sides cannot exist")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def get_area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c


# алгоритм наследования классов - mro(). usage - print(Square.mro())
