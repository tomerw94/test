import hearthstonespell

class shrink(hearthstonespell.Spell):

    def __init__(self):
        super().__init__(self)

        self.mana = 5
        self.text = "turn all the minion's\nstats to 1,1"
        self.name = "Shrink"


    """def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)"""

    def activate(self, game):

        for enemy in game.players[1 - game.current_turn].board:
            enemy.attack = 1
            enemy.max_health = 1
            enemy.health = 1
        for minion in game.players[game.current_turn].board:
            minion.attack = 1
            minion.max_health = 1
            minion.health = 1
