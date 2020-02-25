import hearthstonespell

class assasinate(hearthstonespell.Spell):

    def __init__(self):
        super().__init__(self)
        #super().__init__(type, mana, text, name)

        self.mana = 5
        self.text = "destroy an enemy minion"
        self.name = "assasinate"
        self.targetable = True

    """def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)"""

    def activate(self, game, target):

        game.kill(target - 1)

    def get_targets(self, game):
        targets = []
        for minion in range(len(game.players[1 - game.current_turn].board)):
            targets.append(minion + 8)
        return targets
