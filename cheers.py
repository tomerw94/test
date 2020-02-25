import hearthstonespell

class cheers(hearthstonespell.Spell):

    def __init__(self):
        super().__init__(self)

        self.mana = 1
        self.text = "Give all the minions in\nyour hand +1,+1"
        self.name = "Cheers!"


    """def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)"""

    def activate(self, game):

        for card in game.players[game.current_turn].hand:
            if card.type == "minion":
                card.max_health += 1
                card.health += 1
                card.attack += 1
