import pygame
from player import Player


class Game:

    def __init__(self, screen):

        self.all_players1 = pygame.sprite.Group()
        self.player1 = Player(self, 200, "assets/perso1_right.png", "assets/perso1_right.png", "assets/perso1_left.png", 0, 20, "assets/perso1_right_attaque1.png", "assets/perso1_left_attaque1.png", "assets/perso1_right_attaque2.png", "assets/perso1_left_attaque2.png", 50, -25, 40, 0, 0)
        self.all_players1.add(self.player1)

        self.all_players2 = pygame.sprite.Group()
        self.player2 = Player(self, 600, "assets/perso2_left.png", "assets/perso2_right.png", "assets/perso2_left.png", 880, 20, "assets/perso2_right_attaque1.png", "assets/perso2_left_attaque1.png", "assets/perso2_right_attaque2.png", "assets/perso2_left_attaque2.png", 20, -40, 13, 680, 0)
        self.all_players2.add(self.player2)

        self.player1.other_player(self.all_players2)
        self.player2.other_player(self.all_players1)

        self.pressed = {}
        self.all_jumps = pygame.sprite.Group()

        self.screen = screen

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def get_other(self, comp):
        if comp == self.player1:
            return self.player2
        elif comp == self.player2:
            return self.player1

    def jumping1(self):
        if self.player1.is_jumping == False:
            self.all_jumps.add(self.player1)

    def jumping2(self):
        if self.player2.is_jumping == False:
            self.all_jumps.add(self.player2)

    def coup1(self):
        self.player1.get_coup()

    def coup2(self):
        self.player2.get_coup()

    def super_coup1(self):
        self.player1.get_super_coup()

    def super_coup2(self):
        self.player2.get_super_coup()

    def update(self, screen):
        screen.blit(self.player1.image, self.player1.rect)
        screen.blit(self.player2.image, self.player2.rect)

        self.player1.all_boules.draw(screen)
        self.player2.all_boules.draw(screen)

        if self.pressed.get(pygame.K_d) and self.player1.rect.x < 910:
            self.player1.move_right()
        elif self.pressed.get(pygame.K_q) and self.player1.rect.x > 0:
            self.player1.move_left()

        if self.pressed.get(pygame.K_RIGHT) and self.player2.rect.x < 910:
            self.player2.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player2.rect.x > 0:
            self.player2.move_left()

        for jump in self.all_jumps:
            jump.do_jump()

        for boule in self.player1.all_boules:
            boule.move()
        for boule in self.player2.all_boules:
            boule.move()


        self.player1.update_health_bar(self.screen)
        self.player2.update_health_bar(self.screen)

        self.player1.update_mana_bar(self.screen)
        self.player2.update_mana_bar(self.screen)
