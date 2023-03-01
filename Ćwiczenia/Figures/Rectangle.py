

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        # self.surface = self.a * self.b

    def count_surface_area(self):
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


class Cube(Square):
    def count_surface_area(self):
        return super().count_surface_area() * 6

    def count_volume(self):
        return self.a**3


class Cuboid:
    def __init__(self, rectangle: Rectangle, h):
        self.base = rectangle
        self.hight = h

    def count_surface_area(self):
        return (self.base.count_surface_area() * 2) + (2 * self.base.a * self.hight) + \
            (2 * self.base.b * self.hight)

    def count_volume(self):
        return self.base.count_surface_area() * self.hight
