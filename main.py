from matplotlib.backend_bases import MouseEvent
from numpy import tri
import pygame
from sys import exit

from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((40,40), pygame.SRCALPHA, 32)
        self.image = pygame.image.load("media\\player2.png").convert_alpha();
        #self.image.fill("green") # testing_purpose

        self.rect = self.image.get_rect()
        self.rect.center = CENTER

        self.angle = 0

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

        

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50, 50))
        self.image.fill("green")  # testing_purpose

        self.rect = self.image.get_rect()
        self.rect.center = CENTER

        self.mask = pygame.mask.from_surface(self.image)


def main():
    # ============================INIT VALUES============================
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)

    clock = pygame.time.Clock()
    font = pygame.font.Font("media\\font.ttf", 32)
    background_surface = pygame.image.load("media\\background.jpg").convert()
    score_surface = font.render("score:", True, "white")
    sprite_list = pygame.sprite.Group()
    asteroid_list = pygame.sprite.Group()

    # ====Player====
    player = Player()
    sprite_list.add(player)

    test = Asteroid()
    asteroid_list.add(test)
    sprite_list.add(test)

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()

        screen.blit(background_surface, (0, 0))
        screen.blit(score_surface, (10, 10))

        pygame.draw.polygon(surface=screen, color=(255, 255, 255), points=[
                            (50, 100), (100, 50), (150, 100)])

        sprite_list.draw(screen)

        if pygame.sprite.collide_mask(player, test):
            test.image.fill("red")
        else:
            test.image.fill("green")

        sprite_list.update()

        pygame.display.update()


if __name__ == "__main__":
    main()
