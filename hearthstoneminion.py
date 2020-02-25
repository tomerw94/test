import hearthstonecard
class Minion(hearthstonecard.Card):
    def __init__(self, text="", targetable=False,rarity="common",taunt=False,
                 deathrattle=False, type="minion", battlecry=False,
                 frozen=False, can_attack=False, trolled=False, trolled_attack=0, trolled_health=0,
                 when_friendly_card_played=False, end_of_friendly_turn=False):
        #super().__init__(type, mana, text, name)
        self.type = "minion"
        self.mana = 11
        self.text = ""
        self.name = "None"
        self.attack = -1
        self.max_health = -1
        self.health = -1
        self.can_attack = False
        self.targetable = False
        self.battlecry = False
        self.rarity = "common"
        self.frozen = 0
        self.taunt = False
        self.trolled = False
        self.trolled_attack = 0
        self.trolled_health = 0
        self.end_of_friendly_turn = False
        self.when_friendly_card_played = False
        self.deathrattle = False


    def guitext(self):
        if self.trolled:
            return "%s\nmana: X\nA:(%d) | H(%d)" % ("TROLLED", self.trolled_attack, self.trolled_health)
        else:
            return "%s\nmana: %d\nA:(%d) | H(%d)" % (self.name, self.mana, self.attack, self.health)

    def gui_enemy_text(self):

        return "%s\nmana: %d\nA:(%d) | H(%d)" % (self.name, self.mana, self.attack, self.health)


