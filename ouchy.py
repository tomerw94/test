import hearthstonespell

class ouchy(hearthstonespell.Spell):

    def __init__(self):
        super().__init__(self)

        self.mana = 1
        self.text = "Deal 1 damage to everything"
        self.name = "Ouchy!"


    """def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)"""

    def activate(self, game):

        for enemy in range(len(game.players[1 - game.current_turn].board)):
            game.damage(1, enemy + 8)
        for enemy in range(len(game.players[game.current_turn].board)):
            game.damage(1, enemy + 1)
        game.damage(1, 0)
        game.damage(1, 15)
