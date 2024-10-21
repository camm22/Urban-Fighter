import pygame
from game import Game


def fin(k):
    if k == 1:
        print("")


def jouer1(screen, background):
    clock = pygame.time.Clock()
    FPS = 100
    game = Game(screen)

    running = True

    while running:

        screen.blit(background, (0, 0))

        game.update(screen)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture du jeu")

            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

                if event.key == pygame.K_z:
                    game.jumping1()
                if event.key == pygame.K_UP:
                    game.jumping2()

                if event.key == pygame.K_r:
                    game.coup1()
                if event.key == pygame.K_KP1:
                    game.coup2()

                if event.key == pygame.K_t:
                    game.super_coup1()
                if event.key == pygame.K_KP2:
                    game.super_coup2()

            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

        if (game.player1.fin_de_partie == True) or (game.player2.fin_de_partie == True):
            running = False

    if game.player1.fin_de_partie == True:
        fin(2)
    else:
        fin(1)

    clock.tick(FPS)



def jouer2(screen, background):
    pass