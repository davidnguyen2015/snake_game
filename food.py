import pygame
import random
from settings import *

class Food:
    def __init__(self):
        self.position = (random.randint(0, WIDTH - CELL_SIZE) // CELL_SIZE * CELL_SIZE,
                         random.randint(0, HEIGHT - CELL_SIZE) // CELL_SIZE * CELL_SIZE)
        self.color = RED

    def randomize_position(self):
        self.position = (random.randint(0, WIDTH - CELL_SIZE) // CELL_SIZE * CELL_SIZE,
                         random.randint(0, HEIGHT - CELL_SIZE) // CELL_SIZE * CELL_SIZE)

    def draw(self, surface):
        rect = pygame.Rect(self.position, (CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(surface, self.color, rect)
