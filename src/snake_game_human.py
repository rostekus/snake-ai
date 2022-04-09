import pygame
import sys
import random
from pygame import Vector2


# TODO: reset game , ask user, show score, show max score


CELL_SIZE = 10
CELL_NUMBER = 50
FONT_COLOR = (255, 255, 255)  # white
SCREEN_COLOR = (0, 0, 0)  # black
SNAKE_COLOR = (0, 255, 0)  # green
FRUIT_COLOR = (255, 0, 0)  # red


# pygame config

pygame.init()
pygame.display.set_caption("")
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)


class Game:
    def __init__(self):
        self.game_over = False
        self.score = 0
        self.screen = pygame.display.set_mode(
            (CELL_SIZE * CELL_NUMBER, CELL_SIZE * CELL_NUMBER)
        )
        self.clock = pygame.time.Clock()
        # self.font = pygame.font.Font('font.ttf', 25) # OpenSans-Italic

        # Fruit
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.fruit_color = FRUIT_COLOR
        self.pos = Vector2(self.x, self.y)

        # Snake
        self.head_x = 5
        self.head_y = 2
        self.body = [
            Vector2(self.head_x, self.head_y),
            Vector2(self.head_x + 1, self.head_y),
            Vector2(self.head_x + 1, self.head_y),
        ]
        self.direction = Vector2(1, 0)

        self.snake_color = SNAKE_COLOR

    def play_step(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                self.move_()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord("w"):
                    if self.direction.y != 1:
                        self.direction = Vector2(0, -1)
                if event.key == pygame.K_RIGHT or event.key == ord("d"):
                    if self.direction.x != -1:
                        self.direction = Vector2(1, 0)
                if event.key == pygame.K_DOWN or event.key == ord("s"):
                    if self.direction.y != -1:
                        self.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT or event.key == ord("a"):
                    if self.direction.x != 1:
                        self.direction = Vector2(-1, 0)

        self.is__eaten()

        if self.is_collision():
            self.game_over = True

        self.update_screen()

    def is_collision(self):
        if self.body[0].x >= CELL_NUMBER or self.body[0].x < 0:
            return True
        if self.body[0].y >= CELL_NUMBER or self.body[0].y < 0:
            return True
        if self.body[0] in self.body[1:]:
            return True

        return False

    def is__eaten(self):
        if self.x == self.body[0].x and self.y == self.body[0].y:
            self.new()
            self.ate_()
            self.score += 1

    def update_screen(self):
        self.screen.fill(SCREEN_COLOR)

        self.draw()
        self.draw_()

        # text = self.font.render("Score: " + str(self.score), True, FONT_COLOR)
        # self.screen.blit(text, [0, 0])

        pygame.display.update()
        self.clock.tick(60)

    def draw(self):
        _rect = pygame.Rect(
            int(self.pos.x * CELL_SIZE),
            int(self.pos.y * CELL_SIZE),
            CELL_SIZE,
            CELL_SIZE,
        )
        pygame.draw.rect(self.screen, self.fruit_color, _rect)

    def new(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
        self.draw_()

    def draw_(self):
        for block in self.body:
            block_rect = pygame.Rect(
                int(block.x * CELL_SIZE), int(block.y * CELL_SIZE), CELL_SIZE, CELL_SIZE
            )
            pygame.draw.rect(self.screen, self.snake_color, block_rect)

    def move_(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def new_(self):
        pygame.time.delay(300)
        self.head_x = 5
        self.head_y = 2
        self.body = [
            Vector2(self.head_x, self.head_y),
            Vector2(self.head_x + 1, self.head_y),
            Vector2(self.head_x + 1, self.head_y + 2),
        ]
        self.direction = Vector2(1, 0)

    def ate_(self):
        self.body.append(self.body[-1])


if __name__ == "__main__":
    game = Game()
    while not game.game_over:
        game.play_step()

    print(game.score)
