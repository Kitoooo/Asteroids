import pygame
from config import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, group, player):
        pygame.sprite.Sprite.__init__(self, group)
        print("pew pew")
        self.image = pygame.Surface((4, 4))
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.position = pygame.math.Vector2(player.position)
        self.rect.center = self.position
        self.direction = pygame.math.Vector2(player.direction)

    def update(self):
        self.rect.center = self.position
        self.position -= self.direction*10
        self.checkBundaries()

    def checkBundaries(self):
        if self.position[0] > SCREEN_WIDTH+10:
            self.kill()
        elif self.position[0] < -10:
            self.kill()
        elif self.position[1] > SCREEN_HEIGHT+10:
            self.kill()
        elif self.position[1] < -10:
            self.kill()
