import hearthstonespell

class blessed_heal(hearthstonespell.Spell):

    def __init__(self):
        #super().__init__(type, mana, text, name)
        self.type = "spell"
        self.mana = 0
        self.text = 'Heal your hero +1.\nDraw a card.'
        self.name = "Blessed Heal"
        self.targetable = False

    """def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)"""

    def activate(self, game):

        game.heal(1, 0)
        game.players[game.current_turn].draw(1)
