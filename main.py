from sys import exit

import pygame

from Asteroid import *
from Bullet import *
from config import *
from Player import *


def main():
    # ============================INIT VALUES============================
    pygame.init()

    global isRunning
    isRunning = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)

    score = 0
    clock = pygame.time.Clock()
    font = pygame.freetype.Font("media\\font.ttf", 48)
    background_surface = pygame.image.load("media\\background.jpg").convert()
    sprite_list = pygame.sprite.Group()
    asteroid_list = pygame.sprite.Group()
    bullet_list = pygame.sprite.Group()
    counter = 0
    # ==========Player=========
    player = Player(sprite_list)
    # =====INITIAL ASTEROIDS===
    for i in range(1, 20):
        ast = Asteroid(sprite_list, asteroid_list)

    # ============================MAIN LOOP============================
    while isRunning:
        clock.tick(60)
        counter += 1
        # ===========CONTROLS============
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.forward()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.angle_speed = -5
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.angle_speed = 5
                elif event.key == pygame.K_SPACE:
                    sprite_list.add(Bullet(bullet_list, player))
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    player.angle_speed = 0
        if player.isAlive():
            # ===========BACKGROUND===========
            screen.blit(background_surface, (0, 0))

            if counter >= 60:
                Asteroid(sprite_list, asteroid_list)
                counter = 0
            # ===========RENDERING============
            sprite_list.draw(screen)

            # ===========COLLISION============
            for ast in asteroid_list:
                for bullet in bullet_list:
                    if pygame.sprite.collide_rect(bullet, ast):
                        ast.kill()
                        bullet.kill()
                        score += 1
                        print(f"score: {score}")
                if pygame.sprite.collide_mask(player, ast):
                    print("collide with"+str(ast))
                    ast.kill()
                    player.hp -= 1

            # ============SCORE HP=============
            font.render_to(screen, (10, 10),
                           f"score: {score}", (255, 255, 255))
            hp_rect = font.get_rect(f"hp: {player.hp}")
            hp_rect.topright = (SCREEN_WIDTH-10, 10)
            font.render_to(screen, hp_rect,
                           f"hp: {player.hp}", (255, 255, 255))

            sprite_list.update()
        else:
            # ============GAMEOVER=============
            screen.fill("black")
            text = "GAME OVER !"
            score_txt = f"score: {score}"
            gameover_rect = font.get_rect(text, size=62)
            gameover_rect.midbottom = CENTER
            score_rect = font.get_rect(score_txt, size=62)
            score_rect.midtop = (CENTER_X, CENTER_Y+10)
            font.render_to(screen, gameover_rect, text,
                           (255, 255, 255), size=62)
            font.render_to(screen, score_rect, score_txt,
                           (255, 255, 255), size=62)

        pygame.display.update()


if __name__ == "__main__":
    main()
