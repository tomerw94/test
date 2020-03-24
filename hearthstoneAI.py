import hearthstonegame
import copy
"""ZOMBIE = "z"
CAR = "c"
ICE_CREAM = "i"
EMPTY = "*"
DOLLAR = "$"
"""

import pickle

TRADE = 1
matches = 0
def possible_actions(state):
    attackerINDEX = find_attacker_index(state)
    if attackerINDEX == -1:
        return []
    att = state.game.players[state.game.current_turn].board[attackerINDEX].attack
    health = state.game.players[state.game.current_turn].board[attackerINDEX].health
    POS_temp = []
    POS_temp.append(FACE)
    for minion in state.game.players[1 - state.game.current_turn].board:
        if minion.attack < health:
            if minion.health <= att:
                if KILL_SURVIVE not in POS_temp:
                    POS_temp.append(KILL_SURVIVE)
            else:
                if ENJURE_SURVIVE not in POS_temp:
                    POS_temp.append(ENJURE_SURVIVE)
        else:
            if minion.health <= att:
                if TRADE not in POS_temp:
                    POS_temp.append(TRADE)
            else:
                if ENJURE_DIE not in POS_temp:
                    POS_temp.append(ENJURE_DIE)
    POS = [2, 1, 3, 4, 0]
    for i in range(len(ACTIONS)):
        if len(ACTIONS) - 1 - i not in POS_temp:
            POS.pop(POS.index(len(ACTIONS) - 1 - i))
    return POS

def find_attacker_index(state):
    for minion in range(len(state.game.players[state.game.current_turn].board)):
        if state.game.players[state.game.current_turn].board[minion].can_attack:
            return minion
    return -1


FACE = 0
TRADE = 1
KILL_SURVIVE = 2
ENJURE_DIE = 3
ENJURE_SURVIVE = 4
ACTIONS = [FACE, TRADE, KILL_SURVIVE, ENJURE_DIE, ENJURE_SURVIVE]


N_FRIENDLY_MINIONS_LOW = 0  # 0-2
N_FRIENDLY_MINIONS_MED = 1  # 3-4
N_FRIENDLY_MINIONS_HIGH = 2  # 5-7

N_ENEMY_MINIONS_LOW = 0  # 0-2
N_ENEMY_MINIONS_MED = 1  # 3-4
N_ENEMY_MINIONS_HIGH = 2  # 5-7

FRIENDLY_MINIONS_ATTACK_LOW = 0  # 0-5
FRIENDLY_MINIONS_ATTACK_LOWMED = 1  # 6-10
FRIENDLY_MINIONS_ATTACK_MED = 2  # 11-15
FRIENDLY_MINIONS_ATTACK_HIGH = 3  # 15+

FRIENDLY_MINIONS_HEALTH_LOW = 0  # 0-5
FRIENDLY_MINIONS_HEALTH_LOWMED = 1  # 6-10
FRIENDLY_MINIONS_HEALTH_MED = 2  # 11-15
FRIENDLY_MINIONS_HEALTH_HIGH = 3  # 15+

HEALTH_LOW_LOW = 0  # 0-5
HEALTH_LOW_HIGH = 1  # 6-10
HEALTH_MED_LOW = 2  # 11-15
HEALTH_MED_HIGH = 3  # 16-20
HEALTH_HIGH_LOW = 4  # 21-25
HEALTH_HIGH_HIGH = 5  # 26-30

ENEMY_HEALTH_LOW_LOW = 0  # 0-5
ENEMY_HEALTH_LOW_HIGH = 1  # 6-10
ENEMY_HEALTH_MED_LOW = 2  # 11-15
ENEMY_HEALTH_MED_HIGH = 3  # 16-20
ENEMY_HEALTH_HIGH_LOW = 4  # 21-25
ENEMY_HEALTH_HIGH_HIGH = 5  # 26-30

ENEMY_MINIONS_ATTACK_LOW = 0  # 0-5
ENEMY_MINIONS_ATTACK_LOWMED = 1  # 6-10
ENEMY_MINIONS_ATTACK_MED = 2  # 11-15
ENEMY_MINIONS_ATTACK_HIGH = 3  # 15+

ENEMY_MINIONS_HEALTH_LOW = 0  # 0-5
ENEMY_MINIONS_HEALTH_LOWMED = 1  # 6-10
ENEMY_MINIONS_HEALTH_MED = 2  # 11-15
ENEMY_MINIONS_HEALTH_HIGH = 3  # 15+

"""grid = [
    [DOLLAR, EMPTY, EMPTY, ICE_CREAM],
    [EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY],
    [ZOMBIE, EMPTY, EMPTY, CAR]
]"""

def get_new_learning_game():
    return hearthstonegame.Game(-1)

starting_game_state = get_new_learning_game()


"""for row in grid:
    print(' '.join(row))"""

# no presentation

class WideState():

    def __init__(self, state):

        self.attacker = state.attacker
        self.N_minions = state.N_minions
        self.N_E_minions = state.N_E_minions
        self.F_M_A = state.F_M_A
        self.E_M_A = state.E_M_A
        self.F_M_H = state.F_M_H
        self.E_M_H = state.E_M_H
        self.Health = state.Health
        self.E_Health = state.E_Health
        self.attacker_index = state.attacker_index
        self.POS = state.POS

    def __eq__(self, other):
        """print(self.POS)
        print(other.POS)
        print("^eq^")"""
        #return self.POS == other.POS
        return isinstance(other, WideState) and self.POS == other.POS and \
               self.E_Health == other.E_Health and \
               self.attacker == other.attacker and \
               self.Health == other.Health and \
               self.N_E_minions == other.N_E_minions and \
               self.N_minions == other.N_minions and \
               self.E_M_H == other.E_M_H and \
               self.E_M_A == other.E_M_A and \
               self.F_M_A == other.F_M_A and \
               self.F_M_H == other.F_M_H
               #self.attacker_index == other.attacker_index and \



    def __hash__(self):
        return hash(str(self.Health) + str(self.E_Health))

    def __str__(self):
        return f"{self.attacker_index},{self.attacker},{self.POS},{self.F_M_A},{self.F_M_H},{self.E_M_A},{self.E_M_H}," \
               f"{self.E_Health},{self.N_E_minions},{self.N_minions},{self.Health}"

class State:
    """def __init__(self, grid, car_pos):
        self.grid = grid
        self.car_pos = car_pos"""

    def __init__(self, game):

        self.game = game
        self.POS = []
        self.attacker_index = find_attacker_index(self)
        self.attacker = [-1, -1]
        if len(game.players[game.current_turn].board) > 0:
            #print("test")
            #print("attacker index = %d" % self.attacker_index)
            #print(len(state.game.players[state.game.current_turn].board))
            if game.players[game.current_turn].board[self.attacker_index].attack < 3:
                self.attacker[0] = 0
            elif game.players[game.current_turn].board[self.attacker_index].attack < 6:
                self.attacker[0] = 1
            else:
                self.attacker[0] = 2
            if game.players[game.current_turn].board[self.attacker_index].health < 3:
                self.attacker[1] = 0
            elif game.players[game.current_turn].board[self.attacker_index].health < 6:
                self.attacker[1] = 1
            else:
                self.attacker[1] = 2
        self.N_minions = len(game.players[game.current_turn].board)
        self.N_E_minions = len(game.players[1 - game.current_turn].board)
        FminionsAttackSum = 0
        for minion in game.players[game.current_turn].board:
            FminionsAttackSum += minion.attack
        if FminionsAttackSum < 6:
            self.F_M_A = 0
        elif FminionsAttackSum < 11:
            self.F_M_A = 1
        elif FminionsAttackSum < 16:
            self.F_M_A = 2
        else:
            self.F_M_A = 3

        FminionsHealthkSum = 0
        for minion in game.players[game.current_turn].board:
            FminionsHealthkSum += minion.health
        if FminionsHealthkSum < 6:
            self.F_M_H = 0
        elif FminionsHealthkSum < 11:
            self.F_M_H = 1
        elif FminionsHealthkSum < 16:
            self.F_M_H = 2
        else:
            self.F_M_H = 3

        EminionsAttackSum = 0
        for minion in game.players[1 - game.current_turn].board:
            EminionsAttackSum += minion.attack
        if EminionsAttackSum < 6:
            self.E_M_A = 0
        elif EminionsAttackSum < 11:
            self.E_M_A = 1
        elif EminionsAttackSum < 16:
            self.E_M_A = 2
        else:
            self.E_M_A = 3

        EminionsHealthSum = 0
        for minion in game.players[1 - game.current_turn].board:
            EminionsHealthSum += minion.health
        if EminionsHealthSum < 6:
            self.E_M_H = 0
        elif EminionsHealthSum < 11:
            self.E_M_H = 1
        elif EminionsHealthSum < 16:
            self.E_M_H = 2
        else:
            self.E_M_H = 3

        if game.players[game.current_turn].health < 6:
            self.Health = 0
        elif game.players[game.current_turn].health < 11:
            self.Health = 1
        elif game.players[game.current_turn].health < 16:
            self.Health = 2
        elif game.players[game.current_turn].health < 21:
            self.Health = 3
        elif game.players[game.current_turn].health < 26:
            self.Health = 4
        else:
            self.Health = 5

        if game.players[1 - game.current_turn].health < 6:
            self.E_Health = 0
        elif game.players[1 - game.current_turn].health < 11:
            self.E_Health = 1
        elif game.players[1 - game.current_turn].health < 16:
            self.E_Health = 2
        elif game.players[1 - game.current_turn].health < 21:
            self.E_Health = 3
        elif game.players[1 - game.current_turn].health < 26:
            self.E_Health = 4
        else:
            self.E_Health = 5

        self.POS = possible_actions(self)
        #print("self.pos: ", self.POS)


        self.wide_state = WideState(self)
        self.wide_string = self.wide_state.Health
    """def __eq__(self, other):
        return isinstance(other, State) and self.grid == other.grid and self.car_pos == other.car_pos"""
    def __eq__(self, other):

        #return isinstance(other, State) and len(self.game.players[self.game.current_turn].board) == len(other.game.players[other.game.current_turn].board)
        return isinstance(other, State) and self.game == other.game


    def play_cards(self):
        for attempt in range(self.game.players[self.game.current_turn].left_mana + 1):
            for card in range(len(self.game.players[self.game.current_turn].hand)):
                #print("card = %d" % card)
                #print("players length = %d"  % len(self.game.players))
                #print("current_turn = %d" % self.game.current_turn)
                if self.game.players[self.game.current_turn].hand[card].mana == self.game.players[self.game.current_turn].left_mana - attempt and (len(self.game.players[self.game.current_turn].board) < 7 or self.game.players[self.game.current_turn].hand[card].type != "minion"):
                    self.game.play(card, 9)
                    self.play_cards()
                    return



    def do_noob_turn(self):
        for i in range(2):
            if self.game.players[i].health < 1:
                self.game.end_turn()
        for minion in range(len(self.game.players[self.game.current_turn].board)):
            self.game.attack(minion + 1, 15)
        self.play_cards()
        self.game.end_turn()

    def calculate_reward(self):
        minions_number_reward = 8 * len(self.game.players[self.game.current_turn].board)
        enemy_minions_number_reward = - (100 * len(self.game.players[1 - self.game.current_turn].board))
        minions_total_attack_reward = self.F_M_A
        minions_total_health_reward = self.F_M_H
        enemy_minions_total_attack_reward = -20 * self.E_M_A
        enemy_minions_total_health_reward = - 10 * self.E_M_H
        health_reward = 4 * (self.game.players[self.game.current_turn].health - 30)
        if health_reward <= -120:
            health_reward = -1500
        enemy_health_reward = 4 * (30 - self.game.players[1 - self.game.current_turn].health)
        if enemy_health_reward >= 120:
            enemy_health_reward = 1500
        cards_in_hand_reward = 3 * (len(self.game.players[self.game.current_turn].hand) - 3)
        cards_in_enemy_hand_reward = -4 * (len(self.game.players[1 - self.game.current_turn].hand) - 3)
        temp = minions_number_reward + enemy_minions_number_reward + minions_total_attack_reward + minions_total_health_reward + enemy_minions_total_attack_reward + enemy_minions_total_health_reward + health_reward + enemy_health_reward + cards_in_hand_reward + cards_in_enemy_hand_reward
        return temp



    """def __hash__(self):
        return hash(str(self.grid) + str(self.car_pos))"""

    def __hash__(self):
        return hash(str(self.game))

    """def __str__(self):
        return f"State(grid={self.grid}, car_pos={self.car_pos})"""

    def __str__(self):
        return f"State(game={self.game})"


start_state = State(game=starting_game_state)

from copy import deepcopy



def get_trade_target(state, attacker):
    attacker_att = state.game.players[state.game.current_turn].board[attacker].attack
    attacker_health = state.game.players[state.game.current_turn].board[attacker].health
    sum = attacker_att + attacker_health
    target_size = -1
    target = -1
    for minion in range(len(state.game.players[1 - state.game.current_turn].board)):
        e_m_a = state.game.players[1 - state.game.current_turn].board[minion].attack
        e_m_h = state.game.players[1 - state.game.current_turn].board[minion].health
        if e_m_a >= attacker_health and e_m_h <= attacker_att:
            if e_m_h + e_m_a > target_size:
                target = minion
                target_size = e_m_a + e_m_h
    return target

def get_enj_and_survive(state, attacker):
    attacker_att = state.game.players[state.game.current_turn].board[attacker].attack
    attacker_health = state.game.players[state.game.current_turn].board[attacker].health
    for minion in range(len(state.game.players[1 - state.game.current_turn].board)):
        if state.game.players[1 - state.game.current_turn].board[minion].attack < attacker_health and state.game.players[1 - state.game.current_turn].board[minion].health > attacker_att:
            return minion
    return -1

def get_kill_and_survive(state, attacker):
    max_att = -1
    target = -1
    attacker_att = state.game.players[state.game.current_turn].board[attacker].attack
    attacker_health = state.game.players[state.game.current_turn].board[attacker].health
    for minion in range(len(state.game.players[1 - state.game.current_turn].board)):
        e_m_a = state.game.players[1 - state.game.current_turn].board[minion].attack
        e_m_h = state.game.players[1 - state.game.current_turn].board[minion].health
        if e_m_a < attacker_health and e_m_h <= attacker_att:
            if e_m_a > max_att:
                max_att = e_m_a
                target = minion

    return target

def get_enj_and_die(state, attacker):
    attacker_att = state.game.players[state.game.current_turn].board[attacker].attack
    attacker_health = state.game.players[state.game.current_turn].board[attacker].health
    for minion in range(len(state.game.players[1 - state.game.current_turn].board)):
        if state.game.players[1 - state.game.current_turn].board[minion].attack >= attacker_health and state.game.players[1 - state.game.current_turn].board[minion].health > attacker_att:
            return minion
    return -1


def act(state, action):

    """def new_car_pos(state, action):
        p = deepcopy(state.car_pos)
        attacker = attacker_index(state)
        if action == FACE:
            state.game.attack(attacker, 15)
        elif action == TRADE:
            target = get_trade_target(state, attacker)
            state.game.attack(attacker, target + 7)
        elif action == KILL_SURVIVE:
            target = get_kill_and_survive(state, attacker)
            state.game.attack(attacker, target + 7)
        elif action == ENJURE_DIE:
            target = get_enj_and_die(state, attacker)
            state.game.attack(attacker, target + 7)
        else:
            raise ValueError(f"Unknown action {action}")
        return p"""

    def new_game_state(state, action):

        if action == FACE:
            state.game.attack(state.attacker_index + 1, 15)
        elif action == ENJURE_SURVIVE:
            target = get_enj_and_survive(state, state.attacker_index)
            state.game.attack(state.attacker_index + 1, target + 8)
        elif action == TRADE:
            target = get_trade_target(state, state.attacker_index)
            state.game.attack(state.attacker_index + 1, target + 8)
        elif action == KILL_SURVIVE:
            target = get_kill_and_survive(state, state.attacker_index)
            state.game.attack(state.attacker_index + 1, target + 8)
        elif action == ENJURE_DIE:
            target = get_enj_and_die(state, state.attacker_index)
            state.game.attack(state.attacker_index + 1, target + 8)
        else:
            raise ValueError(f"Unknown action {action}")
        while find_attacker_index(state) == -1:

            if state.game.players[1 - state.game.current_turn].health < 1 or state.game.players[state.game.current_turn].health < 1:
                return state

            state.play_cards()
            state.game.end_turn()
            if state.game.GameId == -2:
                break
            state.do_noob_turn()
            state = State(state.game)

        return state

    start_state = new_game_state(state, action)


    """if grid_item == ZOMBIE:
        reward = -100
        is_done = True
        new_grid[p[0]][p[1]] += CAR
    elif grid_item == DOLLAR:
        reward = 1000
        is_done = True
        new_grid[p[0]][p[1]] += CAR
    elif grid_item == ICE_CREAM:
        reward = 500
        is_done = True
        new_grid[p[0]][p[1]] += CAR
    elif grid_item == EMPTY:
        reward = -1
        is_done = False
        old = state.car_pos
        new_grid[old[0]][old[1]] = EMPTY
        new_grid[p[0]][p[1]] = CAR
    elif grid_item == CAR:
        reward = -1
        is_done = False
    else:
        raise ValueError(f"Unknown grid item {grid_item}")"""
    reward = state.calculate_reward()
    if state.game.players[state.game.current_turn].health < 1 or state.game.players[1 - state.game.current_turn].health < 1:
        is_done = True
    else:
        is_done = False

    return State(state.game), reward, is_done

#import numpy as np
import random

#random.seed(42)  # for reproducibility

# N_STATES = 16
N_EPISODES = 0

MAX_EPISODE_STEPS = 10000

MIN_ALPHA = 1

#alphas = np.linspace(1.0, MIN_ALPHA, N_EPISODES)
alphas = []
for i in range(N_EPISODES):
    alphas.append((1.0 - MIN_ALPHA) * (1 - (i / N_EPISODES)) + MIN_ALPHA)
gamma = 1.0
eps = 0.0
print("loading")
q_ready = pickle.load(open("qtable-1584340730.pickle", "rb"))
print("finished loading")
q_table = q_ready
print(len(q_table), "<- length of q_table")


def q(wide_string, action=None):
    print("in q(), len is %d" % len(q_table))
    #temp = q(state.wide_state).index(max(q(state.wide_state)))

    if wide_string not in q_table:

        for s in q_table:
            if s.__eq__(wide_string):
                if action is None:
                    return q_table[s]
                return q_table[s][s.POS.index(action)]


        zeros = []
        for i in range(len(wide_string.POS)):
            zeros.append(0)

        q_table[wide_string] = zeros

    if action is None:
        return q_table[wide_string]

    return q_table[wide_string][wide_string.POS.index(action)]

def choose_action(state):

    """if state.attacker_index == -1:
        state.play_cards()
        state.game.end_turn()
        state.do_noob_turn()
        choose_action(state)
        return"""
    state.POS = possible_actions(state)
    state.wide_state.POS = state.POS
    POSSIBILITIES = state.wide_state.POS
    while len(POSSIBILITIES) == 0:
        """print("nothing to do")"""
        state.play_cards()
        state.game.end_turn()
        if state.game.GameId == -2:
            break
        state.do_noob_turn()
        state.POS = possible_actions(state)
        state = State(state.game)
        state.POS = possible_actions(state)
        state.wide_state.POS = state.POS
        POSSIBILITIES = state.wide_state.POS
        #print(("possibilities: ", POSSIBILITIES))

    if random.uniform(0, 1) < eps:
        #print("random action from -> ", POSSIBILITIES)

        return random.choice(POSSIBILITIES)

    else:
        #return np.argmax(q(state))
        #print(q(state.wide_state).index(max(q(state.wide_state))), state.POS)
        state.POS = possible_actions(state)
        state.wide_state.POS = state.POS

        #temp = q(state.wide_state).index(max(q(state.wide_state)))
        print(q(state.wide_state), "<-q(state.wide_state)")
        print(state.wide_state.POS, "<-POS")
        print(state.wide_state.N_E_minions, "<-NE")
        if len(state.wide_state.POS) < len(q(state.wide_state)):
            temp = 0
        else:
            temp = state.wide_state.POS[q(state.wide_state).index(max(q(state.wide_state)))]

#        print("after q2 ->", state.POS)
        """if temp not in state.POS:
            print("enemy:")
            for m in state.game.players[1 - state.game.current_turn].board:
                print("[%d,%d]" % (m.attack, m.health))
            print("player:")
            for m in state.game.players[state.game.current_turn].board:
                print("[%d,%d]" % (m.attack, m.health))
            print("TEST2")
            print(state.attacker_index)
            print("temp: %d" % temp)
            print("state.POS: ", state.POS)"""

        return temp


bugs = 0
matches = 0
moves = 0
for e in range(N_EPISODES):

    state = State(get_new_learning_game())
    for i in range(2):
        state.game.players[i].maxhealth = 30
        state.game.players[i].health = state.game.players[i].maxhealth
    hand = []
    deck = []
    for minion in state.game.players[state.game.current_turn].hand:
        hand.append([minion.name, minion.mana])
    for minion in state.game.players[state.game.current_turn].deck:
        deck.append(minion.name)
    """print("hand: ")
    print(hand)
    print("deck:")
    print(deck)"""

    total_reward = 0
    reward = 0
    alpha = alphas[e]

    for _ in range(MAX_EPISODE_STEPS):
        #state.POS = possible_actions(state)
        """print("1: ", state.POS)
        state.POS = possible_actions(state)
        print("1: ", state.POS)"""

        action = choose_action(state)
        state.POS = possible_actions(state)
        state.wide_state.POS = state.POS
        q_temp_var = copy.deepcopy(state.wide_state)

        em = []
        fm = []
        for minion in state.game.players[state.game.current_turn].board:
            fm.append([minion.attack, minion.health, minion.name])
        for minion in state.game.players[1 -state.game.current_turn].board:
            em.append([minion.attack, minion.health, minion.name])
        print(state.game.players[1 - state.game.current_turn].health)
        print(em)
        print(fm)
        print(state.game.players[state.game.current_turn].health, state.game.players[state.game.current_turn].left_mana)
        print("2: ", action, state.POS)

        next_state, reward, done = act(state, action)
        while next_state.POS == []:

            if next_state.game.players[1 - next_state.game.current_turn].health < 1 or next_state.game.players[next_state.game.current_turn].health < 1:

                next_state = state
                break
            next_state.play_cards()
            next_state.game.end_turn()
            if next_state.game.GameId == -2:
                break
            next_state.do_noob_turn()

            next_state.POS = possible_actions(state)
            next_state.wide_state.POS = next_state.POS


        if action not in state.POS:

            bugs += 1

        """q(state)[action] = q(state, action) + \
                           alpha * (reward + gamma * np.max(q(next_state)) - q(state, action))"""
        """q(state.wide_state)[action] = q(state.wide_state, action) + \
                           alpha * (reward + gamma * max(q(next_state.wide_state)) - q(state.wide_state, action))"""
        """if len(q(next_state.wide_state)) == 0:
            q(q_temp_var)[q_temp_var.POS.index(action)] = q(q_temp_var, action) + \
                                                          alpha * (reward + 0 - q(q_temp_var, action))
        else:
            q(q_temp_var)[q_temp_var.POS.index(action)] = q(q_temp_var, action) + \
                                      alpha * (reward + gamma * max(q(next_state.wide_state)) - q(q_temp_var,
                                                                                                  action))"""
        q(q_temp_var)[q_temp_var.POS.index(action)] = q(q_temp_var, action) + \
                                                      alpha * (reward + gamma * max(q(next_state.wide_state)) - q(
            q_temp_var,
            action))
        #print(state.POS, "<- state.pos after q")
        if done:
            print("player health: %d\nenemy health: %d" % (state.game.players[state.game.current_turn].health, state.game.players[1 - state.game.current_turn].health))
            break
        state = next_state
        """print(q(state.wide_state))
        print(state.wide_string)"""
        moves += 1
    print(f"Episode {e + 1}: total reward -> {reward}")
"""for s in q_table:
    print(s)"""
print("moves: ", moves)
print("len of q_table: %d" % len(q_table))
import time
import pickle
with open(f"qtable-{int(time.time())}.pickle", "wb") as f:
    pickle.dump(q_table, f)
"""for s in q_table:
    print(s)"""
