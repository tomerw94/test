import hearthstoneminion


class blue_eyes_white_dragon(hearthstoneminion.Minion):

    def __init__(self):
        super().__init__(self)
        self.battlecry = True
        self.mana = 4
        self.max_health = 1
        self.attack = 4
        self.health = self.max_health
        self.text = "Battlecry: Gain 1 health\nfor each other card in\nyour hand."
        self.name = "Blue Eyes White Dragon"
        self.rarity = "rare"

    def activate(self, game):

        bonus = len(game.players[game.current_turn].hand)
        self.max_health += bonus
        self.health = self.max_health
