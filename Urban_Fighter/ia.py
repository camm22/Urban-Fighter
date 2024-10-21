from random import randint

def saut():
    chance = randint(0, 50)
    if chance in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        return True
    else:
        return False

def attaque2():
    return True

def marche_left(game):

    if game.player2.health > 70:
            return True
    elif game.player2.health <=70:
        chance = randint(0, 101)
        if chance >= 0  and chance <= 70:
            return True
        else:
            return False
    elif game.player2.health <=50:
        chance = randint(0, 101)
        if chance >= 0  and chance <= 30:
            return True
        else:
            return False


def marche_right(game):
    if game.player2.health <= 30:
        return True
    elif game.player2.health <= 50:
        chance = randint(0, 101)
        if chance >= 0 and chance <= 70:
            return True
        else:
            return False
    elif game.player2.health > 70:
        chance = randint(0, 101)
        if chance >= 0 and chance <= 30:
            return True
        else:
            return False
