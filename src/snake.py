import config
from vector import Vector
import numpy as np


class Snake:
    def __init__(self):
        self.x = 5
        self.y = 2
        self.body = [
            Vector(self.x, self.y),
            Vector(self.x - 1, self.y),
            Vector(self.x - 2, self.y),
            Vector(self.x - 3, self.y),
            Vector(self.x - 4, self.y),
        ]
        self.direction = Vector(1, 0)

        self.color = config.SNAKE_COLOR

    @property
    def head(self):
        return self.body[0]

    @head.getter
    def head(self):
        return self.body[0]

    # check?
    def move(self, action):
        directions = [Vector(1, 0), Vector(0, -1), Vector(-1, 0), Vector(0, 1)]

        i = directions.index(self.direction)
        if np.array_equal(action, [0, 1, 0]):  # right turn r -> d -> l -> u
            self.direction = directions[(i + 1) % 4]

        elif np.array_equal(action, [0, 0, 1]):
            self.direction = directions[(i - 1) % 4]

        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def ate_fruit(self):
        self.body.append(self.body[-1])
