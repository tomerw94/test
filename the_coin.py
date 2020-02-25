import hearthstonespell

class the_coin(hearthstonespell.Spell):

    def __init__(self, type="spell", targetable=False):
        super().__init__(self)
        #super().__init__(type, mana, text, name)

        self.mana = 0
        self.text = "Gain 1 mana for this turn only"
        self.name = "The Coin"


    """def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)"""

    def activate(self, game):

        game.players[game.current_turn].left_mana += 1
