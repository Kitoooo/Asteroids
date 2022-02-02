import pygame

from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("media\\player2.png").convert_alpha()
        # self.image.fill("green") # testing_purpose

        self.rect = self.image.get_rect()
        self.rect.center = CENTER

        self.angle = 0

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


if __name__ == "__main__":
    raise Exception("It should've been ran")
