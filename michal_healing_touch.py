import hearthstonespell


class michal_healing_touch(hearthstonespell.Spell):

    def __init__(self):
        # super().__init__(type, mana, text, name)
        self.type = "spell"
        self.mana = 3
        self.text = "Heal your hero +10 health"
        self.name = "Michal's Healing Touch"
        self.targetable = False

    def activate(self, game):

        heal = 10
        game.heal(heal, 0)
