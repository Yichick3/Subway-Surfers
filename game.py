import pygame
import sys
import random

from player import Player
from obstacle import Obstacle
from coin import Coin
from power_up import PowerUp

class Game:
    def __init__(self):
        self.player = Player()
        self.obstacles = [Obstacle()]
        self.coins = [Coin()]
        self.power_ups = [PowerUp()]
        self.score = 0

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            self.player.move(keys)

            for obstacle in self.obstacles:
                obstacle.move()
                if obstacle.x < 0:
                    self.obstacles.remove(obstacle)

            for coin in self.coins:
                coin.move()
                if coin.x < 0:
                    self.coins.remove(coin)

            for power_up in self.power_ups:
                power_up.move()
                if power_up.x < 0:
                    self.power_ups.remove(power_up)

            if random.random() < 0.05:
                self.obstacles.append(Obstacle())
            if random.random() < 0.1:
                self.coins.append(Coin())
            if random.random() < 0.05:
                self.power_ups.append(PowerUp())

            screen.fill((255, 255, 255))
            pygame.draw.rect(screen, (255, 0, 0), (self.player.x, self.player.y, self.player.width, self.player.height))
            for obstacle in self.obstacles:
                pygame.draw.rect(screen, (0, 0, 255), (obstacle.x, obstacle.y, obstacle.width, obstacle.height))
            for coin in self.coins:
                pygame.draw.rect(screen, (255, 255, 0), (coin.x, coin.y, coin.width, coin.height))
            for power_up in self.power_ups:
                pygame.draw.rect(screen, (0, 255, 0), (power_up.x, power_up.y, power_up.width, power_up.height))

            pygame.display.flip()
            clock.tick(60)

game = Game()
game.run()
