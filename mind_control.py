import hearthstonespell

class mind_control(hearthstonespell.Spell):

    def __init__(self):
        #super().__init__(type, mana, text, name)
        self.type = "spell"
        self.mana = 10
        self.text = "take control of enemy's left-most minion"
        self.name = "mind control"
        self.targetable = False

    """def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)"""

    def activate(self, game):

        game.players[game.current_turn].board.append(game.players[1 - game.current_turn].board[0])
        game.players[1 - game.current_turn].board.pop(0)
        game.players[game.current_turn].board[-1].can_attack = False