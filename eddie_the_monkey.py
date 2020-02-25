import hearthstoneminion

class eddie_the_monkey(hearthstoneminion.Minion):

    def __init__(self):
        super().__init__(self)
        self.type = "minion"
        self.battlecry = False
        self.mana = 2
        self.max_health = 1
        self.attack = 1
        self.health = self.max_health
        self.can_attack = False
        self.text = "Deathrattle: Summon a\n3,3 Dolphin"
        self.name = "Eddie the Monkey"
        self.targetable = False
        self.rarity = "legendary"
        self.taunt = False
        self.frozen = 0
        self.trolled = False
        self.trolled_attack = 0
        self.trolled_health = 0
        self.end_of_friendly_turn = False
        self.deathrattle = True

    def activate_deathrattle(self, game, player):
        dolphin = hearthstoneminion.Minion()
        dolphin.mana = 3
        dolphin.max_health = 3
        dolphin.attack = 3
        dolphin.health = dolphin.max_health
        dolphin.name = "Eddie's Dolphin"
        game.players[player].summon(dolphin)




