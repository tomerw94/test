import hearthstonespell

class frostball(hearthstonespell.Spell):

    def __init__(self):
        super().__init__(self)
        #super().__init__(type, mana, text, name)

        self.mana = 2
        self.text = "Deal 3 Damage to a\ncharacter, and freeze it"
        self.name = "frostball"
        self.targetable = True

    """def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)"""

    def activate(self, game, target):
        print("frostball targeting %d" % target)
        game.damage(3, target)
        game.freeze(target, 1)

    def get_targets(self, game):
        targets = []
        for minion in range(len(game.players[1 - game.current_turn].board)):
            targets.append(minion + 8)
        for minion in range(len(game.players[game.current_turn].board)):
            targets.append(minion + 1)
        targets.append(0)
        targets.append(15)
        return targets
