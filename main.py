import pygame
from sys import exit

from config import *


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)

    clock = pygame.time.Clock()
    font = pygame.font.Font(ASTEROIDS_FONT, 32)

    text_surface = font.render("test", True, "white")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(text_surface, (10, 10))

        pygame.display.update()


if __name__ == "__main__":
    main()
