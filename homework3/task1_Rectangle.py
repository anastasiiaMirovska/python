# Створити клас Rectangle:
# -він має приймати дві сторони x, y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

from typing import Self


class Rectangle:
    __slots__ = ('x_side', 'y_side')

    def __init__(self, x_side: int | float, y_side: int | float) -> None:
        self.x_side = x_side
        self.y_side = y_side

    def area(self) -> int | float:
        return self.x_side * self.y_side

    def __add__(self, other: Self) -> int | float:
        if isinstance(other, Rectangle):
            return self.area() + other.area()

    def __sub__(self, other: Self) -> int | float:
        if isinstance(other, Rectangle):
            return self.area() - other.area()

    def __eq__(self, other: Self) -> bool:
        if isinstance(other, Rectangle):
            return self.area() == other.area()

    def __ne__(self, other: Self) -> bool:
        if isinstance(other, Rectangle):
            return self.area() != other.area()

    def __lt__(self, other) -> bool:
        if isinstance(other, Rectangle):
            return self.area() < other.area()

    def __gt__(self, other) -> bool:
        if isinstance(other, Rectangle):
            return self.area() > other.area()

    def __len__(self) -> int | float:
        return self.x_side + self.y_side


rect1 = Rectangle(3, 5)
rect2 = Rectangle(2, 4)
print("rect1 + rect2: ", rect1 + rect2)
print("rect1 - rect2: ", rect1 - rect2)
print("rect2 == rect1: ", rect2 == rect1)
print("rect2 != rect1: ", rect2 != rect1)
print("rect1 < rect2: ", rect1 < rect2)
print("rect1 > rect2: ", rect1 > rect2)
print("len(rect1): ", len(rect1))
print("len(rect2): ", len(rect2))
