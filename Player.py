import pygame

from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.original_image = pygame.image.load("media\\player2.png").convert_alpha()
        self.image = pygame.image.load("media\\player2.png").convert_alpha()
        # self.image.fill("green") # testing_purpose

        self.rect = self.image.get_rect(center = CENTER)

        self.angle = 0

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.rotate()

    def rotate(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center = self.rect.center)
        self.mask = pygame.mask.from_surface(self.image )


if __name__ == "__main__":
    raise Exception("It should've been ran")
