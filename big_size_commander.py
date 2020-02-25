import hearthstoneminion


class big_size_commander(hearthstoneminion.Minion):

    def __init__(self):
        super().__init__(self)
        self.mana = 6
        self.max_health = 5
        self.attack = 4
        self.health = self.max_health
        self.text = "In the end of your turn,\ngive all the minions in\nyour hand +2,+2."
        self.name = "Big-Size Commander"
        self.rarity = "epic"
        self.end_of_friendly_turn = True


    def active_end_of_friendly_turn(self, game):
        for card in game.players[game.current_turn].hand:
            if card.type == "minion":
                card.max_health += 2
                card.health += 2
                card.attack += 2


