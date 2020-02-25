import hearthstonespell

class flamestrike(hearthstonespell.Spell):

    def __init__(self):
        #super().__init__(type, mana, text, name)
        self.type = "spell"
        self.mana = 7
        self.text = "Deal 4 damage to all enemy minions"
        self.name = "Flamestrike"
        self.targetable = False

    """def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)"""

    def activate(self, game):

        for enemy in range(len(game.players[1 - game.current_turn].board)):
            game.damage(4, enemy + 8)