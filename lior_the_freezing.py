import hearthstoneminion


class lior_the_freezing(hearthstoneminion.Minion):

    def __init__(self):
        super().__init__(self)
        self.type = "minion"
        self.battlecry = True
        self.mana = 6
        self.max_health = 9
        self.attack = 0
        self.health = self.max_health
        self.can_attack = False
        self.text = "Taunt, Battlecry:\nFreeze all minions\nfor 3 turns."
        self.name = "Lior the Freezing"
        self.targetable = False
        self.rarity = "legendary"
        self.taunt = True
        self.frozen = 0
        self.trolled = False
        self.trolled_attack = 0
        self.trolled_health = 0
        self.end_of_friendly_turn = False
    def activate(self, game):

        for i in range(2):
            for minion in game.players[i].board:
                minion.frozen = 3
                minion.can_attack = False
