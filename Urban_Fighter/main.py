import pygame, sys
from button import Button
from pygame import mixer
from game import Game
from ia import*

pygame.init()


SCREEN = pygame.display.set_mode((980,350))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/map1.png")
BG_GAME = pygame.image.load("assets/map2.png")
BG_OPT = pygame.image.load("assets/map3.png")

tete_player1 = pygame.image.load("assets/tete_perso1.png")
tete_player1_rect = tete_player1.get_rect(center=(325,35))

tete_player2 = pygame.image.load("assets/tete_perso2.png")
tete_player2_rect = tete_player1.get_rect(center=(640,40))

def fin(k):
    if k == 1:
        print("Le joueur 1 a gagné !"),
    else:
        print("Le joueur 2 a gagné !")

def get_font(ital,gras,size):
    return pygame.font.SysFont("Onyx",size, bold=gras, italic=ital)

def Joueur1():

    pygame.display.set_caption("1 Joueur")
    # music
    mixer.music.load("assets/combat_zik.mp3")
    mixer.music.play(-1)  # le -1 permet de jouer la musique en boucle

    clock = pygame.time.Clock()
    FPS = 100
    game = Game(SCREEN)

    running = True

    while running:

        SCREEN.blit(BG, (0, 0))

        SCREEN.blit(tete_player1,tete_player1_rect)
        SCREEN.blit(tete_player2, tete_player2_rect)

        game.update(SCREEN)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

                if event.key == pygame.K_z:
                    game.jumping1()
                if event.key == pygame.K_r:
                    game.coup1()
                if event.key == pygame.K_t:
                    game.super_coup1()


            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False


            if saut():
                game.jumping2()
            if attaque2():
                game.super_coup2()
            if marche_right(game):
                game.player2.move_right()
            if marche_left(game):
                game.player2.move_left()

        if (game.player1.fin_de_partie == True) or (game.player2.fin_de_partie == True):
            running = False

    if game.player1.fin_de_partie == True:
        fin(2)
    else:
        fin(1)

    clock.tick(FPS)

def Joueur2():
    pygame.display.set_caption("2 Joueurs")
    # music
    mixer.music.load("assets/combat_zik.mp3")
    mixer.music.play(-1)  # le -1 permet de jouer la musique en boucle

    clock = pygame.time.Clock()
    FPS = 100
    game = Game(SCREEN)

    running = True

    while running:

        SCREEN.blit(BG, (0, 0))

        SCREEN.blit(tete_player1, tete_player1_rect)
        SCREEN.blit(tete_player2, tete_player2_rect)


        game.update(SCREEN)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

                if event.key == pygame.K_z:
                    game.jumping1()
                if event.key == pygame.K_UP:
                    game.jumping2()

                if event.key == pygame.K_r:
                    game.coup1()
                if event.key == pygame.K_l:
                    game.coup2()

                if event.key == pygame.K_t:
                    game.super_coup1()
                if event.key == pygame.K_m:
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

def options():
    pygame.display.set_caption("Options")
    # music
    mixer.music.load("assets/menu_zik2.mp3")
    mixer.music.play(-1)  # le -1 permet de jouer la musique en boucle

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.blit(BG_OPT,(0,0))
        SCREEN.fill("#9AA4AF")

        OPT_TEXT = get_font(True,False,80).render("Controle :", True, "#b80a0a")
        OPT_RECT = OPT_TEXT.get_rect(center=((470, 50)))

        #OPTION J1
        OPT_J1 = get_font(True,False,50).render("*** JOUEUR 1   ***", True,"#b80a0a" )
        OPT_J1_RECT = OPT_J1.get_rect(center=((200,120)))

        OPT_MOUV_J1 = get_font(False,False,30).render("** Z : Avancez    ** Q : Gauche    ** S : Reculez   ** D : Droite", True, "#1B68BE")
        OPT_MOUV_J1_RECT = OPT_MOUV_J1.get_rect(center=((230,200)))

        OPT_ATT_J1 = get_font(False, False, 30).render("** R : Attaque basique    ** T : Fire Ball", True, "#1B68BE")
        OPT_ATT_J1_RECT = OPT_ATT_J1.get_rect(center=((210, 240)))

        #OPTION J2
        OPT_J2 = get_font(True, False, 50).render("*** JOUEUR 2   ***", True, "#b80a0a")
        OPT_J2_RECT = OPT_J2.get_rect(center=((750, 120)))

        OPT_MOUV_J2 = get_font(False, False, 30).render("** FLECHE_UP : Avancez    ** FLECHE_LEFT : Gauche", True, "#1B68BE")
        OPT_MOUV_J2_RECT = OPT_MOUV_J2.get_rect(center=((730, 200)))

        OPT_MOUVP2_J2 = get_font(False, False, 30).render("** FLECHE_DOWN : Reculez   ** FLECHE_RIGHT : Droite", True, "#1B68BE")
        OPT_MOUVP2_J2_RECT = OPT_MOUVP2_J2.get_rect(center=((730, 240)))

        OPT_ATT_J2 = get_font(False, False, 30).render("** NUM1 : Attaque basique    ** NUM2 : Fire Ball", True, "#1B68BE")
        OPT_ATT_J2_RECT = OPT_ATT_J1.get_rect(center=((710, 280)))

        OPT_BACK = Button(image=pygame.image.load("assets/bouton_encadrement_back.png"), pos=(30, 20), text_input="BACK", font=get_font(False,False,20), base_color="#b80a0a",
                           hovering_color="orange")

        SCREEN.blit(OPT_TEXT, OPT_RECT)
        SCREEN.blit(OPT_J1, OPT_J1_RECT)
        SCREEN.blit(OPT_MOUV_J1, OPT_MOUV_J1_RECT)
        SCREEN.blit(OPT_ATT_J1, OPT_ATT_J1_RECT)

        SCREEN.blit(OPT_J2, OPT_J2_RECT)
        SCREEN.blit(OPT_MOUV_J2, OPT_MOUV_J2_RECT)
        SCREEN.blit(OPT_ATT_J2, OPT_ATT_J2_RECT)
        SCREEN.blit(OPT_MOUVP2_J2, OPT_MOUVP2_J2_RECT)

        OPT_BACK.changeColor(PLAY_MOUSE_POS)
        OPT_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPT_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    pygame.display.set_caption("Menu")
    # music
    mixer.music.load("assets/menu_zik.mp3")
    mixer.music.set_volume(0.3)
    mixer.music.play(-1)  # le -1 permet de jouer la musique en boucle

    while True:

        SCREEN.blit(BG_GAME,(0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(False,False,60).render("URBAN FIGHTER", True, "#b80a0a")
        MENU_RECT = MENU_TEXT.get_rect(center=((490,30)))

        Joueur1_BUTTON = Button(image=pygame.image.load("assets/bouton_encadrement.png"), pos=(263, 107),
                            text_input="1 JOUEUR", font= get_font(False,False,35),base_color="#b80a0a", hovering_color="#ed66a3")
        Joueur2_BUTTON = Button(image=pygame.image.load("assets/bouton_encadrement.png"), pos=(263, 232),
                             text_input="2 JOUEURS", font=get_font(False,False,35), base_color="#b80a0a", hovering_color="#ed66a3")
        OPTION_BUTTON = Button(image=pygame.image.load("assets/bouton_encadrement.png"),pos=(713, 107),
                            text_input="OPTIONS", font= get_font(False,False,35), base_color="#b80a0a", hovering_color="#ed66a3")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/bouton_encadrement.png"), pos=(713,232),
                            text_input="QUIT", font=get_font(False,False,35), base_color="#b80a0a", hovering_color="#ed66a3")

        SCREEN.blit(MENU_TEXT,MENU_RECT)

        for button in [Joueur1_BUTTON,Joueur2_BUTTON, OPTION_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Joueur1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Joueur1()
                if Joueur2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Joueur2()
                if OPTION_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()



