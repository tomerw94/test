import hearthstoneminion


class tamir_poison_master(hearthstoneminion.Minion):

    def __init__(self):
        super().__init__(self)
        self.type = "minion"
        self.battlecry = False
        self.mana = 8
        self.max_health = 5
        self.attack = 6
        self.health = self.max_health
        self.can_attack = False
        self.text = "In the end of your turn,\ndeal 2 damage to all\nenemy minions."
        self.name = "Tamir, Poison Master"
        self.targetable = False
        self.rarity = "legendary"
        self.taunt = False
        self.frozen = 0
        self.trolled = False
        self.trolled_attack = 0
        self.trolled_health = 0
        self.end_of_friendly_turn = True


    def active_end_of_friendly_turn(self, game):
        for minion in range(len(game.players[1 - game.current_turn].board)):
            game.players[1 - game.current_turn].board[minion]
            game.damage(2, minion + 8)

