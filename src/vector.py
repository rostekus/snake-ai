from math import hypot


class Vector:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        self.__x = new_x

    @x.getter
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        self.__y = new_y

    @x.getter
    def y(self):
        return self.__y

    def __add__(self, other):
        cls = type(self)
        return cls(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return all([self.x == other.x, self.y == other.y])

    def __len__(self):
        return hypot(self.x, self.y)

    def __iter__(self):
        yield (self.y, self.x)

    def __repr__(self):
        return rf"Vector({self.x},{self.y})"

    __slots__ = "__x", "__y"
