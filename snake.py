import pygame
from settings import *

class Snake:
    def __init__(self):
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = (0, -CELL_SIZE)
        self.grow = False
        self.score = 0
        self.level = 1
        self.speed = 10

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.direction != (-point[0], -point[1]):
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (cur[0] + x, cur[1] + y)

        if new[0] < 0 or new[0] >= WIDTH or new[1] < 0 or new[1] >= HEIGHT or new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if not self.grow:
                self.positions.pop()
            else:
                self.grow = False

    def reset(self):
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = (0, -CELL_SIZE)
        self.score = 0
        self.level = 1
        self.speed = 10

    def draw(self, surface):
        for pos in self.positions:
            rect = pygame.Rect(pos, (CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(surface, GREEN, rect)
