import hearthstonespell
import random
class armageddon(hearthstonespell.Spell):

    def __init__(self):
        super().__init__(self)
        self.type = "spell"
        self.mana = 6
        self.text = "Deal 20 damage split between all minions"
        self.name = "Armageddon"

    def activate(self, game):
        hits = []
        for boom in range(20):
            size1 = len(game.players[game.current_turn].board)
            size2 = len(game.players[1 - game.current_turn].board)
            if size1 + size2 > 0:
                targets = size1 + size2
                target = random.randint(1, targets)
                if target > size1:

                    game.damage(1, target + 7 - size1)
                    hits.append([game.players[1 - game.current_turn].board[target - size1 - 1].name, "%d->%d" % (
                    game.players[1 - game.current_turn].board[target - size1 - 1].health + 1,
                    game.players[1 - game.current_turn].board[target - size1 - 1].health)])
                else:
                    game.damage(1, target)
                    hits.append([game.players[game.current_turn].board[target - 1].name, "%d->%d" % (game.players[game.current_turn].board[target - 1].health + 1, game.players[game.current_turn].board[target - 1].health)])
                game.update_game()
            else:
                print("OverKill")
        for item in hits:
            print("%s : %s\n"%(item[0], item[1]))