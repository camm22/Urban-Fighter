import pygame
from boule_de_feu import Boule_De_Feu


class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, image_base, image_right, image_left, x_bar, y_bar, image_right_attaque1, image_left_attaque1, image_right_attaque2, image_left_attaque2, cox, coy, a, x_bar_mana, y_bar_mana):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack1 = 5
        self.attack2 = 30
        self.velocity = 2

        self.image_right_attaque1 = image_right_attaque1
        self.image_left_attaque1 = image_left_attaque1
        self.image_right = image_right
        self.image_left = image_left
        self.image_svg = image_base
        self.image = pygame.image.load(image_base)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 200

        self.jump = 2
        self.is_jumping = False
        self.up = True
        self.down = False

        self.all_players = None
        self.other = None

        self.x_bar = x_bar
        self.y_bar = y_bar

        self.image_boule_svg = None
        self.all_boules = pygame.sprite.Group()
        self.image_right_attaque2 = image_right_attaque2
        self.image_left_attaque2 = image_left_attaque2
        self.cox = cox
        self.coy = coy
        self.a = a

        self.percent = 0
        self.percent_speed = 10
        self.percent_svg = 0
        self.verification = True
        self.x_bar_mana = x_bar_mana
        self.y_bar_mana = y_bar_mana
        self.fin_de_partie = False


    def damage(self, amount):
        if amount > self.health:
            self.health = 0
            self.fin_de_partie = True
        else:
            self.health -= amount

    def get_super_coup(self):
        if self.percent >= 70:

            if "right" in self.image_svg:
                self.image_svg = self.image_right_attaque2
                self.image = pygame.image.load(self.image_right_attaque2)
                self.image_boule_svg = "assets/boule_right.png"
            else:
                self.image_svg = self.image_left_attaque2
                self.image = pygame.image.load(self.image_left_attaque2)
                self.image_boule_svg = "assets/boule_left.png"

            self.all_boules.add(Boule_De_Feu(self, self.game, self.image_boule_svg))

            self.percent -= 70

    def get_coup(self):

        if self.percent >= self.percent_svg + 5:
            self.verification = True

        if self.verification:

            if self.percent >= 20:
                self.percent -= 20
                self.percent_svg = self.percent
                self.verification = False

                if "right" in self.image_svg:
                    self.image_svg = self.image_right_attaque1
                    self.image = pygame.image.load(self.image_right_attaque1)
                else:
                    self.image_svg = self.image_left_attaque1
                    self.image = pygame.image.load(self.image_left_attaque1)

                if self.game.check_collision(self, self.all_players):
                    self.other = self.game.get_other(self)
                    self.other.damage(self.attack1)

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def update_mana_bar(self, surface):
        if self.percent <= 100:
            self.add_percent()

        back_bar_color = (0, 0, 0)
        back_bar_position = [self.x_bar_mana, self.y_bar_mana, 300, 10]
        pygame.draw.rect(surface, back_bar_color, back_bar_position, border_radius= 12)

        bar_color = (22, 117, 175)
        bar_position = [self.x_bar_mana, self.y_bar_mana, (300 / 100) * self.percent, 10]
        pygame.draw.rect(surface, bar_color, bar_position, border_radius= 12)

    def update_health_bar(self,surface):
        back_bar_color = (60, 63, 60)
        back_bar_position = [self.x_bar, self.y_bar, self.max_health, 20]
        pygame.draw.rect(surface, back_bar_color, back_bar_position,border_radius= 12)

        bar_color = (111, 210, 46)
        bar_position = [self.x_bar, self.y_bar, self.health, 20]
        pygame.draw.rect(surface, bar_color, bar_position, border_radius= 12)

    def other_player(self, other):
        self.all_players = other

    def do_jump(self):
        self.is_jumping = True

        if self.rect.y == 50:
            self.up = False
            self.down = True

        if self.up == True:
            self.rect.y -= self.jump

        if self.rect.y == 200:
            self.game.all_jumps.remove(self)
            self.is_jumping = False
            self.up = True
            self.down = False

        if self.down == True:
            self.rect.y += self.jump

    def move_right(self):
        self.other = self.game.get_other(self)
        if self.game.check_collision(self, self.all_players):

            if self.rect.center[0] < self.other.rect.center[0]:
                pass
            else:
                self.rect.x += self.velocity
                self.image_svg = self.image_right
                self.image = pygame.image.load(self.image_right)

        else:
            self.rect.x += self.velocity
            self.image_svg = self.image_right
            self.image = pygame.image.load(self.image_right)

    def move_left(self):
        self.other = self.game.get_other(self)
        if self.game.check_collision(self, self.all_players):

            if self.rect.center[0] > self.other.rect.center[0]:
                pass
            else:
                self.rect.x -= self.velocity
                self.image_svg = self.image_left
                self.image = pygame.image.load(self.image_left)

        else:
            self.rect.x -= self.velocity
            self.image_svg = self.image_left
            self.image = pygame.image.load(self.image_left)
