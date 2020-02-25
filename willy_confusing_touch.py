import hearthstonespell


class willy_confusing_touch(hearthstonespell.Spell):

    def __init__(self):
        # super().__init__(type, mana, text, name)
        self.type = "spell"
        self.mana = 2
        self.text = "swap all minion's attack and health"
        self.name = "Willy's confusing touch"
        self.targetable = False

    def activate(self, game):

        for minion in game.players[game.current_turn].board:
            temp = minion.health
            minion.health = minion.attack
            minion.attack = temp

        for minion in game.players[1 - game.current_turn].board:
            temp = minion.health
            minion.health = minion.attack
            minion.attack = temp
