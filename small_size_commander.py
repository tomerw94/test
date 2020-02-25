import hearthstoneminion


class small_size_commander(hearthstoneminion.Minion):

    def __init__(self):
        super().__init__(self)
        self.mana = 2
        self.max_health = 1
        self.attack = 1
        self.health = self.max_health
        self.text = "Battlecry: Give all the\nminions in your hand +1,+1."
        self.name = "Small-size Commander"
        self.rarity = "rare"
        self.battlecry = True


    def activate(self, game):
        for card in game.players[game.current_turn].hand:
            if card.type == "minion":
                card.max_health += 1
                card.health += 1
                card.attack += 1


