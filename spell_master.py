import hearthstoneminion

class spell_master(hearthstoneminion.Minion):

    def __init__(self):
        super().__init__(self)

        self.battlecry = True
        self.mana = 3
        self.max_health = 3
        self.attack = 1
        self.health = self.max_health
        self.text = "Battlecry: Reduce the cost\nof all the spells in your\nhand by 1"
        self.name = "Spell Master"
        self.rarity = "epic"

    def activate(self, game):

        for spell in game.players[game.current_turn].hand:
            if spell.type == "spell":
                if spell.mana > 0:
                    spell.mana -= 1
