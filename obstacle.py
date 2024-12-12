import pygame

class Obstacle(pygame.Rect):
    def __init__(self):
        super().__init__(800, 100, 100, 100)
        self.speed = 5

    def move(self):
        self.x -= self.speed
