import math
class Figure:
    sides_count = 0
    def __init__(self, color=(0, 0, 0), *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = False
        if self.__is_valid_sides(*sides) and len(sides) == self.sides_count:
            self.__sides = list(sides)
        elif self.__is_valid_sides(*sides) and len(sides) == 1:
            self.__sides = [sides[0]] * self.sides_count
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color
    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r = 0, g = 0, b = 0):
        if self.__is_valid_color(r, g, b):
            self.__color = list((r, g, b))

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self, *sides):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__( color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)


    def get_square(self):
        p = sum(self.__sides) / 2
        s = (p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2])) ** 0.5
        return s

class Cube(Figure):
    sides_count = 12
    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10)
triangle1 = Triangle((200, 222, 22), 5, 2)
cube1 = Cube((222, 35, 130), 6)


circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

print(triangle1.get_sides())
print(circle1.get_sides())
print(circle1.get_square())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())
