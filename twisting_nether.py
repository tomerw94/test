import hearthstonespell

class twisting_nether(hearthstonespell.Spell):

    def __init__(self):
        #super().__init__(type, mana, text, name)
        self.type = "spell"
        self.mana = 8
        self.text = "Destroy all minions"
        self.name = "Twisting Nether"
        self.targetable = False

    """def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)"""

    def activate(self, game):

        for minion in range(len(game.players[game.current_turn].board)):
            game.kill(len(game.players[game.current_turn].board) - 1)

        for minion in range(len(game.players[1 - game.current_turn].board)):
            game.kill(len(game.players[1 - game.current_turn].board) + 6)
