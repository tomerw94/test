import hearthstoneminion
import random

class willy_the_troll(hearthstoneminion.Minion):

    def __init__(self):
        super().__init__(self)
        self.type = "minion"
        self.battlecry = True
        self.mana = 3
        self.max_health = 4
        self.attack = 3
        self.health = self.max_health
        self.can_attack = False
        self.text = "Battlecry: TROLL\n(your opponent see\nhis minions wrong)"
        self.name = "Willy the Troll"
        self.targetable = False
        self.rarity = "legendary"
        self.taunt = False
        self.frozen = 0
        self.trolled = False
        self.trolled_attack = 0
        self.trolled_health = 0
        self.end_of_friendly_turn = False

    def activate(self, game):
        random.shuffle(game.players[1 - game.current_turn].board)

        for minion in game.players[1 - game.current_turn].board:
            minion.trolled = True
            minion.trolled_attack = random.randint(0, 10)
            minion.trolled_health = random.randint(1, 10)

