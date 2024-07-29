import pygame
import random
from settings import *

class Fireworks:
    def __init__(self):
        self.fireworks = []
        self.timer = 0

    def trigger(self):
        self.timer = 30  # Duration of the fireworks

    def update(self):
        if self.timer > 0:
            self.timer -= 1
            if len(self.fireworks) < 10:  # Limit the number of fireworks
                x = random.randint(0, WIDTH)
                y = random.randint(0, HEIGHT // 2)  # Fireworks in the upper half of the screen
                color = random.choice(FIREWORK_COLORS)
                self.fireworks.append((x, y, color))

    def draw(self, surface):
        if self.timer > 0:
            for firework in self.fireworks:
                x, y, color = firework
                pygame.draw.circle(surface, color, (x, y), 5)
            self.fireworks = [fw for fw in self.fireworks if fw[1] < HEIGHT // 2 + 50]  # Keep fireworks on screen
