import hearthstoneminion

class golem(hearthstoneminion.Minion):

    def __init__(self):
        super().__init__(self)
        self.type = "minion"
        self.battlecry = False
        self.mana = 1
        self.max_health = 1
        self.attack = 1
        self.health = self.max_health
        self.can_attack = False
        self.text = "Deathrattle: Summon a\n1,1 minion"
        self.name = "Golem"
        self.targetable = False
        self.rarity = "common"
        self.taunt = False
        self.frozen = 0
        self.trolled = False
        self.trolled_attack = 0
        self.trolled_health = 0
        self.end_of_friendly_turn = False
        self.deathrattle = True

    def activate_deathrattle(self, game, player):
        golem_leftovers = hearthstoneminion.Minion()
        golem_leftovers.mana = 1
        golem_leftovers.max_health = 1
        golem_leftovers.attack = 1
        golem_leftovers.health = golem_leftovers.max_health
        golem_leftovers.name = "Golem's leftovers"
        game.players[player].summon(golem_leftovers)




