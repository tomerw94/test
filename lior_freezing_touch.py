import hearthstonespell


class lior_freezing_touch(hearthstonespell.Spell):

    def __init__(self):
        # super().__init__(type, mana, text, name)
        self.type = "spell"
        self.mana = 3
        self.text = "Freeze all enemy\nminions for 1 turn"
        self.name = "Sabri's Freezing Touch"
        self.targetable = False

    def activate(self, game):

        for minion in game.players[1 - game.current_turn].board:
            minion.frozen += 1
