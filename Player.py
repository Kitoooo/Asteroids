import pygame
from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self, group)

        self.original_image = pygame.image.load(
            "media\\player2.png").convert_alpha()
        self.image = pygame.image.load("media\\player2.png").convert_alpha()
        self.rect = self.image.get_rect(center=CENTER)
        self.angle = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.position = pygame.math.Vector2(CENTER)
        self.direction = pygame.math.Vector2(0, 1)
        self.speed = 5
        self.angle_speed = 0
        self.angle = 0
        self.hp = 3

    def update(self):
        self.rotate()
        self.rect.center = self.position

    def rotate(self):
        self.direction.rotate_ip(self.angle_speed)
        self.angle += self.angle_speed
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

    def forward(self):
        self.position -= self.direction*5
        self.checkBoundaries()

    def checkBoundaries(self):
        if self.position[0] > SCREEN_WIDTH+10:
            self.position[0] = -10
        elif self.position[0] < -10:
            self.position[0] = SCREEN_WIDTH+10
        elif self.position[1] > SCREEN_HEIGHT+10:
            self.position[1] = -10
        elif self.position[1] < -10:
            self.position[1] = SCREEN_HEIGHT+10

    def isAlive(self):
        return self.hp > 0


if __name__ == "__main__":
    raise Exception("It should've been ran")
