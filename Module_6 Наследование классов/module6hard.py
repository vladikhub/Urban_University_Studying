import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = list(sides)

        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return all([side > 0 for side in sides])

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum([side for side in self.__sides])

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) and len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            sides = [1]
        super().__init__(color, *sides)
        self.__radius = len(self) / 2 * math.pi

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            sides = [1, 1, 1]
        super().__init__(color, *sides)

    def get_square(self):
        sides = self.get_sides()
        p = len(self) / 2
        return (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))**0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = [1]
        super().__init__(color, *[sides[0] for i in range(12)])

    def get_volume(self):
        sides = self.get_sides()
        return sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())