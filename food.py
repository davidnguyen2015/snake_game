import pygame
import random
from settings import *

class Food:
    def __init__(self):
        self.image = pygame.image.load('apple.png')
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.position = (random.randint(0, WIDTH - CELL_SIZE) // CELL_SIZE * CELL_SIZE,
                         random.randint(0, HEIGHT - CELL_SIZE) // CELL_SIZE * CELL_SIZE)

    def randomize_position(self):
        self.position = (random.randint(0, WIDTH - CELL_SIZE) // CELL_SIZE * CELL_SIZE,
                         random.randint(0, HEIGHT - CELL_SIZE) // CELL_SIZE * CELL_SIZE)

    def draw(self, surface):
        surface.blit(self.image, self.position)
