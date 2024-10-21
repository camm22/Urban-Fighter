import pygame
from math import*

class Boule_De_Feu(pygame.sprite.Sprite):

    def __init__(self, player, game, image_boule_base):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.game = game
        self.image_boule_base = image_boule_base
        self.image = pygame.image.load(image_boule_base)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        if "right" in self.image_boule_base:
            self.rect.x = player.rect.x + player.cox
            self.rect.y = player.rect.y + player.coy
        else:
            self.rect.x = player.rect.x - player.cox + player.a
            self.rect.y = player.rect.y + player.coy



    def remove(self):
        self.player.all_boules.remove(self)

    def move(self):
        if "right" in self.image_boule_base:
            self.rect.x += self.velocity
            self.rect.y += self.velocity/3
        else:
            self.rect.x -= self.velocity
            self.rect.y += self.velocity/3

        if self.game.check_collision(self, self.player.all_players):
            self.player.other = self.game.get_other(self.player)
            self.player.other.damage(self.player.attack2)

            self.remove()

        if self.rect.y > 300:
            self.remove()




