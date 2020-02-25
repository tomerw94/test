import hearthstoneminion

class big_sized_minion(hearthstoneminion.Minion):

    def __init__(self):
        super().__init__(self)
        self.mana = 2
        self.max_health = 4
        self.attack = 4
        self.health = self.max_health
        self.text = "Deathrattle: Deal 5 damage\nto your hero and\nheal enemy hero +5 health"
        self.name = "Big Sized Minion"
        self.rarity = "rare"
        self.deathrattle = True

    def activate_deathrattle(self, game, player):
        if player == game.current_turn:
            game.heal(5, 15)
            game.damage(5, 0)
        else:
            game.heal(5, 0)
            game.damage(5, 15)




