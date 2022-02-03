import pygame

from config import *


class Asteroid(pygame.sprite.Sprite):
    id = 0

    def __init__(self, type=None):
        pygame.sprite.Sprite.__init__(self)
        self.id = Asteroid.id
        Asteroid.id += 1

        if type == None:
            self.image = pygame.Surface((50, 50))
        else:
            self.image = pygame.image.load(
                f"media\\asteroid{type}.png").convert_alpha()

        self.image = pygame.transform.smoothscale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(type*100, 100))

        self.mask = pygame.mask.from_surface(self.image)

    def __str__(self):
        return f"(Asteroid id: {self.id})"
