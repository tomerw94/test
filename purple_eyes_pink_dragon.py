import hearthstoneminion


class purple_eyes_pink_dragon(hearthstoneminion.Minion):

    def __init__(self):
        super().__init__(self)
        self.battlecry = True
        self.mana = 4
        self.max_health = 12
        self.attack = 3
        self.health = self.max_health
        self.text = "Taunt\nBattlecry: Lose 1 health\nfor each other card in\nyour hand."
        self.name = "Purple Eyes Pink Dragon"
        self.rarity = "rare"
        self.taunt = True

    def activate(self, game):

        bonus = len(game.players[game.current_turn].hand)
        self.max_health -= bonus
        self.health = self.max_health