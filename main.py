from sys import exit

import pygame

from Asteroid import *
from config import *
from Player import *


def main():
    # ============================INIT VALUES============================
    pygame.init()
    global isRunning
    isRunning = True
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

    #test = Asteroid()
    for i in range(1, 6):
        ast = Asteroid(i)
        sprite_list.add(ast)
        asteroid_list.add(ast)

    # ============================MAIN LOOP============================
    while isRunning:
        clock.tick(60)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.forward()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.angle_speed = -4
                elif event.key == pygame.K_RIGHT:
                    player.angle_speed = 4

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.angle_speed = 0

        # Drawing background and score
        screen.blit(background_surface, (0, 0))
        screen.blit(score_surface, (10, 10))

        sprite_list.draw(screen)

        for ast in asteroid_list:
            if pygame.sprite.collide_mask(player, ast):
                print("collide with"+str(ast))
                ast.kill()
                player.hp -= 1
                print(player.hp)

        sprite_list.update()
        pygame.display.update()


if __name__ == "__main__":
    main()
