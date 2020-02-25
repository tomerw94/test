import hearthstonespell
import hearthstoneminion
class companion(hearthstonespell.Spell):

    def __init__(self):
        #super().__init__(type, mana, text, name)
        self.type = "spell"
        self.mana = 7
        self.text = "Fill your board with 2,2 minions"
        self.name = "companion"
        self.targetable = False

    """def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)"""

    def activate(self, game):

        while len(game.players[game.current_turn].board) < 7:
            game.players[game.current_turn].board.append(hearthstoneminion.Minion())
            game.players[game.current_turn].board[-1].name = "token"
            game.players[game.current_turn].board[-1].mana = 1
            game.players[game.current_turn].board[-1].attack = 2
            game.players[game.current_turn].board[-1].max_health = 2
            game.players[game.current_turn].board[-1].health = 2
