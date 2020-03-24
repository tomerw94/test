import hearthstoneplayer
import hearthstonecard
import random
import hearthstoneminion
import copy

from cards import blessed_heal
from cards import small_size_commander
from cards import big_size_commander
from cards import blue_eyes_white_dragon
from cards import white_eyes_blue_dragon
from cards import purple_eyes_pink_dragon
from cards import tamir_poison_master
from cards import flamestrike
from cards import michal_the_healer
from cards import willy_confusing_touch
from cards import michal_healing_touch
from cards import mind_control
from cards import tomer_upgrading_touch
from cards import twisting_nether
from cards import on_target
from cards import companion
from cards import lior_the_freezing
from cards import lior_freezing_touch
from cards import willy_the_troll
from cards import tomer_the_builder
from cards import tamir_poisonous_touch
from cards import Growing_Monster
from cards import eddie_the_monkey
from cards import the_coin
from cards import last_explosion
from cards import assasinate
from cards import frostball
from cards import spell_master
from cards import upgrade
from cards import golem
from cards import armageddon
from cards import magic
from cards import ouchy
from cards import shrink
from cards import big_sized_minion
from cards import cheers
"""
"""

class Game:

    def __init__(self, numberofgame):
        self.deathrattles_list = []
        self.guitargets = []
        self.can_heropower = True
        self.target = -1
        self.GameId = numberofgame
        self.started = False
        self.temp_card = hearthstonecard.Card()
        self.current_turn = 0
        self.players = [hearthstoneplayer.Player(), hearthstoneplayer.Player()]
        self.players[0].name = "player 1"
        self.players[1].name = "player 2"
        self.actions_history = []
        if random.randint(0, 1):
            self.current_turn += 1
        self.all_cards = []

        for i in range(2):
            for m in range(7):
                self.all_cards.append(hearthstoneminion.Minion())
                self.all_cards[(7 * i) + m].mana = m + 1
                self.all_cards[(7 * i) + m].text = "a normal and\nboring minion"
                self.all_cards[(7 * i) + m].type = "minion"
                self.all_cards[(7 * i) + m].name = "minion"
                self.all_cards[(7 * i) + m].max_health = random.randint(1, (m + 1) * 2)
                self.all_cards[(7 * i) + m].health = self.all_cards[m].max_health
                self.all_cards[(7 * i) + m].attack = (2 * (m + 1)) - self.all_cards[m].max_health + 1

        self.all_cards.append(small_size_commander.small_size_commander())
        self.all_cards.append(big_size_commander.big_size_commander())
        self.all_cards.append(cheers.cheers())
        self.all_cards.append(golem.golem())
        if self.GameId > -1:
            self.all_cards.append(lior_the_freezing.lior_the_freezing())
            self.all_cards.append(lior_freezing_touch.lior_freezing_touch())
            self.all_cards.append(tomer_the_builder.tomer_the_builder())
        self.all_cards.append(tamir_poison_master.tamir_poison_master())
        self.all_cards.append(tamir_poisonous_touch.tamir_poisonous_touch())
        self.all_cards.append(ouchy.ouchy())
        self.all_cards.append(shrink.shrink())
        self.all_cards.append(on_target.on_target())
        self.all_cards.append(armageddon.armageddon())
        self.all_cards.append(spell_master.spell_master())
        self.all_cards.append(frostball.frostball())
        self.all_cards.append(twisting_nether.twisting_nether())
        self.all_cards.append(big_sized_minion.big_sized_minion())
        self.all_cards.append(flamestrike.flamestrike())
        self.all_cards.append(michal_the_healer.michal_the_healer())
        self.all_cards.append(willy_confusing_touch.willy_confusing_touch())
        self.all_cards.append(mind_control.mind_control())
        self.all_cards.append(tomer_upgrading_touch.tomer_upgrading_touch())
        self.all_cards.append(companion.companion())
        self.all_cards.append(michal_healing_touch.michal_healing_touch())
        self.all_cards.append(willy_the_troll.willy_the_troll())
        self.all_cards.append(Growing_Monster.growing_monster())
        self.all_cards.append(eddie_the_monkey.eddie_the_monkey())
        self.all_cards.append(last_explosion.last_explosion())
        self.all_cards.append(assasinate.assasinate())
        self.all_cards.append(blue_eyes_white_dragon.blue_eyes_white_dragon())
        self.all_cards.append(white_eyes_blue_dragon.white_eyes_blue_dragon())
        self.all_cards.append(purple_eyes_pink_dragon.purple_eyes_pink_dragon())
        self.all_cards.append(magic.magic())
        self.all_minions = []
        self.all_spells = []
        for card in self.all_cards:
            if card.type == "minion":
                self.all_minions.append(card)
            else:
                self.all_spells.append(card)
        self.common_minions = []
        self.rare_minions = []
        self.epic_minions = []
        self.legendary_minions = []
        for minion in self.all_minions:
            if minion.rarity == "common":
                self.common_minions.append(minion)
                #print(minion.name)
            elif minion.rarity == "rare":
                self.rare_minions.append(minion)
            elif minion.rarity == "epic":
                self.epic_minions.append(minion)
            else:
                self.legendary_minions.append(minion)
        #print("cards : %d %d %d %d %d" % (len(self.common_minions), len(self.rare_minions), len(self.epic_minions), len(self.legendary_minions), len(self.all_spells)))

        for i in range(2):
            commonsamples = random.sample(range(0, len(self.common_minions)), 10)
            for number in commonsamples:
                self.players[i].deck.append(copy.deepcopy(self.common_minions[number]))
            raresamples = random.sample(range(0, len(self.rare_minions)), 5)
            for number in raresamples:
                self.players[i].deck.append(copy.deepcopy(self.rare_minions[number]))
            epicsamples = random.sample(range(0, len(self.epic_minions)), 1)
            for number in epicsamples:
                self.players[i].deck.append(copy.deepcopy(self.epic_minions[number]))
            legendarysamples = random.sample(range(0, len(self.legendary_minions)), 4)
            for number in legendarysamples:
                self.players[i].deck.append(copy.deepcopy(self.legendary_minions[number]))
            spellsamples = random.sample(range(0, len(self.all_spells)), 10)
            if self.GameId > -1:
                for number in spellsamples:
                    self.players[i].deck.append(copy.deepcopy(self.all_spells[number]))
            random.shuffle(self.players[i].deck)



        #print("length of deck is ", len(self.players[self.current_turn].deck), " cards")

        self.players[self.current_turn].draw(4)
        self.players[self.current_turn].max_mana = 1
        self.players[self.current_turn].left_mana = self.players[self.current_turn].max_mana
        self.players[1 - self.current_turn].draw(4)
        self.players[1 - self.current_turn].max_mana = 0
        self.players[1 - self.current_turn].hand.append(the_coin.the_coin())


    def add_action(self, current_turn, text):

        self.actions_history.append([current_turn, text])
        if len(self.actions_history) > 10:
            self.actions_history.pop(0)

    def update_game(self):
        player1boardlength = len(self.players[self.current_turn].board)
        for m in range (player1boardlength):
            if self.players[self.current_turn].board[player1boardlength-m-1].health <= 0:
                self.kill(player1boardlength-m-1)

        player2boardlength = len(self.players[1 - self.current_turn].board)
        for m in range(player2boardlength):
            if self.players[1 - self.current_turn].board[player2boardlength - m - 1].health <= 0:
                self.kill(player2boardlength - m + 6)
        if len(self.deathrattles_list) > 0:
            self.deathrattles_list[0][1].activate_deathrattle(self, self.deathrattles_list[0][0])
            self.deathrattles_list.pop(0)
            self.update_game()
        """else:
            fm = []
            for minion in self.players[self.current_turn].board:
                fm.append([minion.attack, minion.health])
            em = []
            for minion in self.players[1 - self.current_turn].board:
                em.append([minion.attack, minion.health])
            print(self.players[1 - self.current_turn].health)
            print(em)
            print(fm)
            print(self.players[self.current_turn].health)"""


    """def get_player_move(self, p):

        return self.moves[p]"""

    def end_turn(self):

        for minion in self.players[self.current_turn].board:
            if minion.end_of_friendly_turn:
                minion.active_end_of_friendly_turn(self)
                self.update_game()

        self.current_turn = 1 - self.current_turn
        self.can_heropower = True
        self.players[self.current_turn].draw(1)
        if self.players[self.current_turn].max_mana < 10:
            self.players[self.current_turn].max_mana += 1
        self.players[self.current_turn].left_mana = self.players[self.current_turn].max_mana
        for minion in self.players[self.current_turn].board:
            if minion.frozen > 0:
                minion.frozen -= 1
                minion.can_attack = False
            else:
                minion.can_attack = True
        if self.players[self.current_turn].frozen > 0:
            self.players[self.current_turn].frozen -= 1
        else:
            self.players[self.current_turn].can_attack = True

        self.update_game()

    def freeze(self, target, amount):
        if target == 0:
            self.players[self.current_turn].frozen += amount
        elif target == 15:
            self.players[1 - self.current_turn].frozen += amount
        elif target < 8:
            self.players[self.current_turn].board[target - 1].frozen += amount
        else:
            self.players[1 - self.current_turn].board[target - 8].frozen += amount

    def damage(self, damage, target):

        if target == 0:
            self.players[self.current_turn].health -= damage
        elif target < 8:
            self.players[self.current_turn].board[target - 1].health -= damage
        elif target < 15:
            self.players[1 - self.current_turn].board[target - 8].health -= damage
        else:
            self.players[1 - self.current_turn].health -= damage

    def heal(self, heal, target):

        if target == 0:
            if self.players[self.current_turn].health + heal < self.players[self.current_turn].maxhealth:
                self.players[self.current_turn].health += heal
            else:
                self.players[self.current_turn].health = self.players[self.current_turn].maxhealth
        elif target < 8:
            if self.players[self.current_turn].board[target - 1].health + heal < self.players[self.current_turn].board[target - 1].max_health:
                self.players[self.current_turn].board[target - 1].health += heal
            else:
                self.players[self.current_turn].board[target - 1].health = self.players[self.current_turn].board[target - 1].max_health
        elif target < 15:
            if self.players[1 - self.current_turn].board[target - 8].health + heal < self.players[1 - self.current_turn].board[
                target - 8].max_health:
                self.players[1 - self.current_turn].board[target - 8].health += heal
            else:
                self.players[1 - self.current_turn].board[target - 8].health = self.players[1 - self.current_turn].board[
                    target - 8].max_health
        else:
            if self.players[1 - self.current_turn].health + heal < self.players[1 - self.current_turn].maxhealth:
                self.players[1 - self.current_turn].health += heal
            else:
                self.players[1 - self.current_turn].health = self.players[1 - self.current_turn].maxhealth

    def kill(self, target):
        #print("prechange target is %d" % target)
        player = self.current_turn
        if target > 6:
            target -= 7
            player = 1 - player
        #print("target is %d and board length is %d" %(target, len(self.players[player].board)))
        #print("current turn is %d" % self.current_turn)
        self.temp_card = self.players[player].board[target]
        self.players[player].board.pop(target)
        if self.temp_card.deathrattle:
            self.deathrattles_list.append([player, self.temp_card])





    def heropower(self):
        print(self.players[self.current_turn].type)
        if self.players[self.current_turn].type == "warlock":
            self.players[self.current_turn].draw(1)
            self.damage(2, 0)
        elif self.players[self.current_turn].type == "michal":
            self.players[self.current_turn].deck.append(blessed_heal.blessed_heal())
            random.shuffle(self.players[self.current_turn].deck)
        self.can_heropower = False
        self.players[self.current_turn].left_mana -= 2
        self.add_action(self.current_turn, " used Hero Power")
        self.update_game()





    def play(self, handloc, target):
        #print("current_turn = ", self.current_turn, " handloc = ", handloc, "target = ", target)
        self.temp_card = self.players[self.current_turn].hand[handloc]
        self.add_action(self.current_turn, " played %s" %self.temp_card.name)
        self.players[self.current_turn].hand.pop(handloc)
        self.players[self.current_turn].left_mana -= self.temp_card.mana
        for minion in self.players[self.current_turn].board:
            if minion.when_friendly_card_played:
                minion.activate_when_friendly_card_played(self)

        self.activate_card(self.temp_card, target)
        self.update_game()
    def activate_card(self, card, target):
        if card.type == "minion":
            if card.battlecry:
                card.activate(self)
            self.players[self.current_turn].board.append(card)

        elif card.type == "spell":
            #print("a spell was activated")
            if card.targetable:
                card.activate(self, target)
            else:
                card.activate(self)

    def attack(self, attacker, target):
        if target == 15:
            target = 0
        else:
            target -= 7

        if attacker > 0:
            if target == 0:
                self.players[1-self.current_turn].health -= self.players[self.current_turn].board[attacker - 1].attack
                self.add_action(self.current_turn, " %s attacked the hero (-%d)" % (self.players[self.current_turn].board[attacker - 1].name, self.players[self.current_turn].board[attacker - 1].attack))
            else:
                self.players[1-self.current_turn].board[target - 1].health -= self.players[self.current_turn].board[attacker - 1].attack
                self.players[self.current_turn].board[attacker - 1].health -= self.players[1-self.current_turn].board[target - 1].attack
                self.add_action(self.current_turn, " %s attacked %s" % (
                self.players[self.current_turn].board[attacker - 1].name,
                self.players[1 - self.current_turn].board[target - 1].attack))
            self.players[self.current_turn].board[attacker - 1].can_attack = False
        else:
            if target == 0:
                self.players[1-self.current_turn].health -= self.players[self.current_turn].attack
                self.add_action(self.current_turn," hero attacked the hero (-%d)" % self.players[self.current_turn].attack)
            else:
                self.players[1-self.current_turn].board[target - 1].health -= self.players[self.current_turn].attack
                self.players[self.current_turn].health -= self.players[1-self.current_turn].board[target - 1].attack
                self.add_action(self.current_turn, " hero attacked %s" % (
                self.players[1 -self.current_turn].board[target - 1].name))

            self.players[self.current_turn].can_attack = False
        self.update_game()

    def connected(self):
        return self.ready

    """def bothWent(self):
        return self.p1Went and self.p2Went"""

    """def winner(self):
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[0].upper()[0]

        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1
        return winner"""

    """def resetWent(self):
        self.p1Went = False
        self.p2Went = False"""
