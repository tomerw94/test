class Player:
    def __init__(self, frozen=False):
        self.frozen = False
        self.type = "None"
        self.name = "empty name"
        self.deck = []
        self.hand = []
        self.board = []
        self.maxhealth = 30
        self.health = self.maxhealth
        self.fatigue = 1
        self.turn = False
        self.playernum = -1
        self.max_mana = 0
        self.left_mana = 0
        self.can_attack = False
        self.attack = 0
    def draw(self, num):

        for c in range(num):
            if len(self.deck) > 0:
                temp = self.deck[-1]
                self.deck.pop(-1)
                if len(self.hand) < 10:
                    self.hand.append(temp)
            else:
                self.health -= self.fatigue
                self.fatigue += 1



    def summon(self, minion):
        if len(self.board) < 7:
            self.board.append(minion)

    def guitext(self):
        return "%s : %d" % (self.type, self.health)
