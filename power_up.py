import pygame

class PowerUp(pygame.Rect):
    def __init__(self):
        super().__init__(800, 300, 30, 30)
        self.speed = 3

    def move(self):
        self.x -= self.speed
