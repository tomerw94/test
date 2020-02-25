import hearthstonespell

class on_target(hearthstonespell.Spell):

    def __init__(self):
        super().__init__(self)
        #super().__init__(type, mana, text, name)

        self.mana = 1
        self.text = "Set a minion's health to 1"
        self.name = "On Target"
        self.targetable = True

    """def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)"""

    def activate(self, game, target):

        if target > 7:
            game.players[1 - game.current_turn].board[target - 8].max_health = 1
            game.players[1 - game.current_turn].board[target - 8].health = 1
        else:
            game.players[game.current_turn].board[target - 1].max_health = 1
            game.players[game.current_turn].board[target - 1].health = 1
    def get_targets(self, game):
        targets = []
        for minion in range(len(game.players[1 - game.current_turn].board)):
            targets.append(minion + 8)
        for minion in range(len(game.players[game.current_turn].board)):
            targets.append(minion + 1)

        return targets
