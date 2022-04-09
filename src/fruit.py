import random
import config
from vector import Vector


class Fruit:
    def __init__(self):
        self.x = random.randint(0, config.CELL_NUMBER - 1)
        self.y = random.randint(0, config.CELL_NUMBER - 1)
        self.color = config.FRUIT_COLOR
        self.pos = Vector(self.x, self.y)

    def new(self):
        self.x = random.randint(0, config.CELL_NUMBER - 1)
        self.y = random.randint(0, config.CELL_NUMBER - 1)
        self.pos = Vector(self.x, self.y)
