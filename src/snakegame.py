import pygame
import numpy as np
from gym import Env
from gym.spaces import Box, discrete
from keras.models import load_model

from vector import Vector
import config
from snake import Snake
from fruit import Fruit

import sys
from math import hypot

# TODO:
# Two Snakes diffrent colors for different nn


class Game(Env):
    def __init__(self, render=False, conv=False):

        self.done = False
        self.score = 0
        self.iter = 0

        # Snake
        self.snake = Snake()
        self.fruit = Fruit()

        self.dist = self.distance(self.snake.head, self.fruit)
        # for RL
        self.reward = 0
        self.action_space = Discrete(3)
        self.observation_space = Box(low=0, high=1, dtype=int, shape=(11,))

        self.state = self.get_state()
        self.head_last_pos = []

        self.conv = conv
        self.game_array = np.zeros((50, 50), dtype=np.int8)

    def step(self, action):
        action == 0
        if action == 0:
            action = [0, 0, 1]
        elif action == 1:
            action = [1, 0, 0]
        else:
            action = [0, 1, 0]

        self.iter += 1

        self.snake.move(action)

        if self.snake.head == self.fruit.pos:
            self.snake.ate_fruit()
            self.fruit.new()
            self.reward += 10
            self.score += 1

        # self.head_last_pos.append((self.snake.head.x,self.snake.head.y))
        # if self.iter >=4 and self.iter %4:
        # 	if (head.x,head.y) in self.head_last_pos:
        # 		self.reward -= 5
        # 		self.head_last_pos = []

        if self.is_collision(pt=None) or self.iter > 20 * len(self.snake.body):
            self.done = True
            self.reward += -10

        self.reward += self.dist_snake_fruit()

        info = {}
        if self.conv:
            self.state = self.get_state_conv()
        else:
            self.state = self.get_state()

        with np.printoptions(threshold=np.inf):
            print(self.get_state_conv())

        return self.state, self.reward, self.done, info

    def dist_snake_fruit(self):
        hypt = self.distance(self.snake.head, self.fruit)
        if hypt > self.dist:
            self.dist = hypt
            return -1
        else:
            self.dist = hypt
            return 1

    def get_state_conv(self):

        for vector in self.snake.body:
            for cords in vector:
                self.game_array[cords] = 1

        x = self.fruit.x
        y = self.fruit.y
        self.game_array[y][x] = 1

    def get_state(self):
        head = self.snake.head

        l = Vector(head.x - 20, head.y)
        r = Vector(head.x + 20, head.y)
        u = Vector(head.x, head.y - 20)
        d = Vector(head.x, head.y + 20)

        dir_r = self.snake.direction == Vector(1, 0)
        dir_u = self.snake.direction == Vector(0, -1)
        dir_l = self.snake.direction == Vector(-1, 0)
        dir_d = self.snake.direction == Vector(0, 1)

        state = [
            # Danger straight
            (dir_r and self.is_collision(pt=r))
            or (dir_l and self.is_collision(pt=l))
            or (dir_u and self.is_collision(pt=u))
            or (dir_d and self.is_collision(pt=d)),
            # Danger right
            (dir_u and self.is_collision(pt=r))
            or (dir_d and self.is_collision(pt=l))
            or (dir_l and self.is_collision(pt=u))
            or (dir_r and self.is_collision(pt=d)),
            # Danger left
            (dir_d and self.is_collision(pt=r))
            or (dir_u and self.is_collision(pt=l))
            or (dir_r and self.is_collision(pt=u))
            or (dir_l and self.is_collision(pt=d)),
            # Move direction
            dir_l,
            dir_r,
            dir_u,
            dir_d,
            # Food location
            self.fruit.x < self.snake.head.x,  # food left
            self.fruit.x > head.x,  # food right
            self.fruit.y < head.y,  # food up
            self.fruit.y > head.y,  # food dowd
        ]
        return np.array(state, dtype=np.int8)

    def is_collision(self, pt=None):

        if pt is None:
            pt = self.snake.head

        if pt.x >= config.CELL_NUMBER or pt.x < 0:

            return True
        if pt.y >= config.CELL_NUMBER or pt.y < 0:

            return True
        if pt in self.snake.body[1:]:
            return True

        return False

    def distance(self, object1, object2):
        return hypot(object1.x - object2.x, object1.y - object2.y)

    def reset(self):
        self.done = False
        self.score = 0
        self.reward = 0
        self.iter = 0

        self.snake = Snake()

        self.fruit = Fruit()

        self.state = self.get_state()

        return self.state

    def render(self, model, nb_of_steps):
        if self.render:
            pygame.init()
            pygame.display.set_caption("")
            SCREEN_UPDATE = pygame.USEREVENT
            pygame.time.set_timer(SCREEN_UPDATE, 150)

            clock = pygame.time.Clock()
            screen = pygame.display.set_mode(
                (
                    config.CELL_SIZE * config.CELL_NUMBER,
                    config.CELL_SIZE * config.CELL_NUMBER,
                )
            )
            # font = pygame.font.Font('font.ttf', 25)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            while True:
                action_arr = model.predict(self.state.reshape(1, 1, 11)).tolist()[0]
                max_value = max(action_arr)

                action = action_arr.index(max_value)

                self.state, self.reward, done, _ = self.step(action)

                screen.fill(config.SCREEN_COLOR)

                for block in self.snake.body:
                    block_rect = pygame.Rect(
                        int(block.x * config.CELL_SIZE),
                        int(block.y * config.CELL_SIZE),
                        config.CELL_SIZE,
                        config.CELL_SIZE,
                    )

                    pygame.draw.rect(screen, self.snake.color, block_rect)

                _rect = pygame.Rect(
                    int(self.fruit.x * config.CELL_SIZE),
                    int(self.fruit.y * config.CELL_SIZE),
                    config.CELL_SIZE,
                    config.CELL_SIZE,
                )

                pygame.draw.rect(screen, self.fruit.color, _rect)
                # text = self.font.render("Score: " + str(self.score), True, FONT_COLOR)
                # self.screen.blit(text, [0, 0])

                pygame.display.update()
                print(done)
                print("\n")
                print(self.snake.head.x, self.snake.head.y)
                print(self.fruit.x, self.fruit.y)
                print("\n")
                if done:
                    self.reset()


if __name__ == "__main__":

    game = Game()
    model = load_model("/model/model.h5")
    game.render(model, 100)
