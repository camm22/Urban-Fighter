import pygame
from jeu import*
pygame.init()



def menu(choix):
    pygame.display.set_caption("Urban Fighter")
    screen = pygame.display.set_mode((980, 350))

    background = pygame.image.load("assets/map1.png")

    if choix == 1:
        jouer1(screen, background)
    elif choix == 2:
        jouer2(screen, background)
    elif choix == 3:
        pass
    else:
        pygame.quit()
        print("Fermeture du jeu")


menu(1)


