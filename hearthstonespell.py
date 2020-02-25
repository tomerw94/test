import hearthstonecard
class Spell(hearthstonecard.Card):
    def __init__(self, type="spell", targetable=False):
        #super().__init__(type, mana, text, name)
        self.type = "spell"
        self.mana = 11
        self.text = "None"
        self.name = "None"
        self.targetable = False

    def guitext(self):
        return "%s\nmana: %d" % (self.name, self.mana)