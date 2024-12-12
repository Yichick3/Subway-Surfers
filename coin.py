import pygame

class Coin(pygame.Rect):
    def __init__(self):
        super().__init__(800, 200, 20, 20)
        self.speed = 2

    def move(self):
        self.x -= self.speed
