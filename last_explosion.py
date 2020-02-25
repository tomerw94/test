import hearthstonespell

class last_explosion(hearthstonespell.Spell):

    def __init__(self):
        super().__init__(self)
        #super().__init__(type, mana, text, name)
        self.targetable = True
        self.mana = 4
        self.text = "Choose a friendly minion.\ndestroy it and deal its\nattack damage to all \nenemy minions"
        self.name = "Last Explosion"


    """def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)"""

    def activate(self, game, target):

        damage = game.players[game.current_turn].board[target - 1].attack
        for minion in range(len(game.players[1 - game.current_turn].board)):
            game.damage(damage, minion + 8)
        game.kill(target - 1)

    def get_targets(self, game):
        targets = []
        for minion in range(len(game.players[game.current_turn].board)):
            targets.append(minion + 1)
        return targets
