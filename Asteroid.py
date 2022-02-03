from random import randint, uniform, choice
import pygame

from config import *


class Asteroid(pygame.sprite.Sprite):
    id = 0

    def __init__(self, group1, group2):
        pygame.sprite.Sprite.__init__(self, group1, group2)
        self.id = Asteroid.id
        Asteroid.id += 1
        self.image = pygame.image.load(
            f"media\\asteroid{str(randint(1,5))}.png").convert_alpha()
        self.size = randint(1, 10)
        self.image = pygame.transform.smoothscale(
            self.image, (20*self.size, 20*self.size))
        random_x = choice(
            [i for i in range(-400, SCREEN_WIDTH+400) if i not in range(0, SCREEN_WIDTH)])
        random_y = choice(
            [i for i in range(-400, SCREEN_HEIGHT+400) if i not in range(0, SCREEN_HEIGHT)])
        self.position = pygame.math.Vector2(random_x, random_y)
        self.randompos = pygame.math.Vector2(pygame.mouse.get_pos())
        self.direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1))
        self.vel = randint(0,6)
        self.rect = self.image.get_rect(center=self.position)

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):

        self.position -= self.direction*self.vel
        self.rect.center = self.position
        self.checkBoundaries()

    def checkBoundaries(self):
        if self.position[0] > SCREEN_WIDTH+400:
            self.position[0] = -400
        elif self.position[0] < -400:
            self.position[0] = SCREEN_WIDTH+400
        elif self.position[1] > SCREEN_HEIGHT+400:
            self.position[1] = -400
        elif self.position[1] < -400:
            self.position[1] = SCREEN_HEIGHT+400

    def __str__(self):
        return f"(Asteroid id: {self.id})"
