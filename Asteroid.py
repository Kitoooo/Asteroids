import pygame

from config import *


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50, 50))
        self.image.fill("green")  # testing_purpose

        self.rect = self.image.get_rect()
        self.rect.center = CENTER

        self.mask = pygame.mask.from_surface(self.image)
