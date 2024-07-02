import math

class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        if isinstance(sides, list) and len(sides) == self.sides_count:
            self.__sides = sides
        else:
            self.__sides = [sides for _ in range(self.sides_count)]
        self.__color = list(color)
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, *args):
        for i in args:
            if not isinstance(i, int) or i > 255 or i < 0:
                return False

        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        for i in args:
            if not isinstance(i, int) and i < 0 and len(args) == len(self.__sides):
                return False
        return True

    def get_sides(self):
        return self.__sides

    def set_sides(self, *args):
        if len(args) == self.sides_count:
            self.__sides = list(args)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = sides / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius**2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__height = math.sqrt(sum(super().get_sides())/2 * (sum(super().get_sides())/2 - super().get_sides()[0]) *
                         (sum(super().get_sides())/2 - super().get_sides()[1]) *
                         (sum(super().get_sides())/2 - super().get_sides()[2]))/ super().get_sides()[0]

    def get_square(self):
        return super().get_sides()[0] * self.__height / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = [sides for _ in range(12)]

    def get_volume(self):
        return self.__sides[0]**3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((33, 26, 12), [4, 5, 6])
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
triangle1.set_color(102, 66, 256)
print(circle1.get_color())
print(cube1.get_color())
print(triangle1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
triangle1.set_sides(13)
print(cube1.get_sides())
print(circle1.get_sides())
print(triangle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
print(circle1.get_square())
print(triangle1.get_square())
