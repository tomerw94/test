import hearthstonespell

class tomer_upgrading_touch(hearthstonespell.Spell):

    def __init__(self):
        #super().__init__(type, mana, text, name)
        self.type = "spell"
        self.mana = 5
        self.text = "give all your minions (+1, +2)"
        self.name = "Tomer's Upgrading Touch"
        self.targetable = False

    """def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)"""

    def activate(self, game):

        for minion in game.players[game.current_turn].board:
            minion.attack += 1
            minion.max_health += 2
            minion.health += 2