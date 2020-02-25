import hearthstoneminion


class growing_monster(hearthstoneminion.Minion):

    def __init__(self):
        super().__init__(self)
        self.type = "minion"
        self.battlecry = False
        self.mana = 3
        self.max_health = 2
        self.attack = 2
        self.health = self.max_health
        self.can_attack = False
        self.text = "Whever you play a\ncard, get +1/+1."
        self.name = "Growing Minion"
        self.targetable = False
        self.rarity = "rare"
        self.taunt = False
        self.frozen = 0
        self.trolled = False
        self.trolled_attack = 0
        self.trolled_health = 0
        self.end_of_friendly_turn = False
        self.when_friendly_card_played = True

    def activate_when_friendly_card_played(self, game):
        self.max_health += 1
        self.health += 1
        self.attack += 1
