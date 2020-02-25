import hearthstonespell

class tamir_poisonous_touch(hearthstonespell.Spell):

    def __init__(self):
        #super().__init__(type, mana, text, name)
        self.type = "spell"
        self.mana = 2
        self.text = "Deal 1 damage to all minions.\nIf any died, repeat"
        self.name = "Tamir's Poisonous\nTouch"
        self.targetable = False

    """def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)"""

    def activate(self, game):
        repeat = False
        for enemy in range(len(game.players[1 - game.current_turn].board)):
            game.damage(1, enemy + 8)
            if repeat == False and game.players[1 - game.current_turn].board[enemy].health == 0:
                repeat = True
        for minion in range(len(game.players[game.current_turn].board)):
            game.damage(1, minion + 1)
            if repeat == False and game.players[game.current_turn].board[minion].health == 0:
                repeat = True
        game.update_game()
        if repeat:
            self.activate(game)
