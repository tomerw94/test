import hearthstonespell
import hearthstoneminion
class magic(hearthstonespell.Spell):

    def __init__(self):
        super().__init__(self)
        #super().__init__(type, mana, text, name)

        self.mana = 3
        self.text = "transform a minion\ninto a 2,3 rabbit\nwith Taunt"
        self.name = "magic"
        self.targetable = True

    """def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)"""

    def activate(self, game, target):
        rabbit = hearthstoneminion.Minion()
        rabbit.attack = 2
        rabbit.max_health = 3
        rabbit.health = rabbit.max_health
        rabbit.taunt = True
        rabbit.text = "Taunt"
        rabbit.name = "Rabbit"
        rabbit.mana = 2
        if target > 7:
            game.players[1 - game.current_turn].board[target - 8] = rabbit
        else:
            game.players[game.current_turn].board[target - 1] = rabbit

    def get_targets(self, game):
        targets = []
        for minion in range(len(game.players[1 - game.current_turn].board)):
            targets.append(minion + 8)
        for minion in range(len(game.players[game.current_turn].board)):
            targets.append(minion + 1)
        return targets
