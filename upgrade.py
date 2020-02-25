import hearthstonespell

class upgrade(hearthstonespell.Spell):

    def __init__(self):
        #super().__init__(type, mana, text, name)
        self.type = "spell"
        self.mana = 3
        self.text = 'Heal your hero +2.\nIf you control Tomer,\ngive it +2,+4 and add\n" \
                    "an "Upgrade! to\n your hand'
        self.name = "Upgrade!"
        self.targetable = False

    """def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)"""

    def activate(self, game):

        game.heal(2, 0)
        counter = 0
        for minion in game.players[game.current_turn].board:
            if minion.name == "Tomer the Builder":
                minion.attack += 2
                minion.max_health += 4
                minion.health += 4
                counter += 1
        if counter > 0:
            game.players[game.current_turn].hand.append(upgrade())
