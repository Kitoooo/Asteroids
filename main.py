from sys import exit

import pygame

from Asteroid import *
from config import *
from Player import *


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

        # Drawing background and score
        screen.blit(background_surface, (0, 0))
        screen.blit(score_surface, (10, 10))

        sprite_list.draw(screen)

        if pygame.sprite.collide_mask(player, test):
            test.image.fill("red")
            player.angle += 0.5
        else:
            test.image.fill("green")

        sprite_list.update()
        pygame.display.update()


if __name__ == "__main__":
    main()
