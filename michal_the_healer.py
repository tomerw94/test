import hearthstoneminion


class michal_the_healer(hearthstoneminion.Minion):

    def __init__(self):
        super().__init__(self)
        self.type = "minion"
        self.battlecry = True
        self.mana = 5
        self.max_health = 3
        self.attack = 3
        self.health = self.max_health
        self.can_attack = False
        self.text = "Battlecry: Double \nyour hero's health\n(max 30)"
        self.name = "Michal the Healer"
        self.targetable = False
        self.rarity = "legendary"
        self.taunt = False
        self.frozen = 0
        self.trolled = False
        self.trolled_attack = 0
        self.trolled_health = 0
        self.end_of_friendly_turn = False
    def activate(self, game):

        heal = game.players[game.current_turn].health
        game.heal(heal, 0)
