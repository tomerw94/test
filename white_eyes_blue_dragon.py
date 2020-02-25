import hearthstoneminion


class white_eyes_blue_dragon(hearthstoneminion.Minion):

    def __init__(self):
        super().__init__(self)
        self.battlecry = True
        self.mana = 5
        self.max_health = 1
        self.attack = 5
        self.health = self.max_health
        self.text = "Battlecry: Gain 1 health\nfor each other card in\nenemy's hand."
        self.name = "White Eyes Blue Dragon"
        self.rarity = "rare"

    def activate(self, game):

        bonus = len(game.players[1 - game.current_turn].hand)
        self.max_health += bonus
        self.health = self.max_health