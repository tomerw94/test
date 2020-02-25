import hearthstoneminion
import upgrade
class tomer_the_builder(hearthstoneminion.Minion):

    def __init__(self):
        super().__init__(self)
        self.type = "minion"
        self.battlecry = True
        self.mana = 2
        self.max_health = 1
        self.attack = 1
        self.health = self.max_health
        self.can_attack = False
        self.text = 'Battlecry: add "upgrade!" \nto your hand.'
        self.name = "Tomer the Builder"
        self.targetable = False
        self.rarity = "legendary"
        self.taunt = False
        self.frozen = 0
        self.trolled = False
        self.trolled_attack = 0
        self.trolled_health = 0
        self.end_of_friendly_turn = False

    def activate(self, game):
        game.players[game.current_turn].hand.append(upgrade.upgrade())

