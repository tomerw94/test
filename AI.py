ZOMBIE = "z"
CAR = "c"
ICE_CREAM = "i"
EMPTY = "*"
DOLLAR = "$"

grid = [
    [DOLLAR, EMPTY, EMPTY, ICE_CREAM],
    [EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY],
    [ZOMBIE, EMPTY, EMPTY, CAR]
]

for row in grid:
    print(' '.join(row))


class State:

    def __init__(self, grid, car_pos):
        self.grid = grid
        self.car_pos = car_pos

    def __eq__(self, other):
        return isinstance(other, State) and self.grid == other.grid and self.car_pos == other.car_pos

    def __hash__(self):
        return hash(str(self.grid) + str(self.car_pos))

    def __str__(self):
        return f"State(grid={self.grid}, car_pos={self.car_pos})"


UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

ACTIONS = [UP, DOWN, LEFT, RIGHT]

start_state = State(grid=grid, car_pos=[3, 3])

from copy import deepcopy


def act(state, action):
    def new_car_pos(state, action):
        p = deepcopy(state.car_pos)
        if action == UP:
            p[0] = max(0, p[0] - 1)
        elif action == DOWN:
            p[0] = min(len(state.grid) - 1, p[0] + 1)
        elif action == LEFT:
            p[1] = max(0, p[1] - 1)
        elif action == RIGHT:
            p[1] = min(len(state.grid[0]) - 1, p[1] + 1)
        else:
            raise ValueError(f"Unknown action {action}")
        return p

    p = new_car_pos(state, action)
    grid_item = state.grid[p[0]][p[1]]

    new_grid = deepcopy(state.grid)

    if grid_item == ZOMBIE:
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
        raise ValueError(f"Unknown grid item {grid_item}")

    return State(grid=new_grid, car_pos=p), reward, is_done

#import numpy as np
import random

random.seed(42)  # for reproducibility

N_STATES = 16
N_EPISODES = 3750

MAX_EPISODE_STEPS = 100

MIN_ALPHA = 1

#alphas = np.linspace(1.0, MIN_ALPHA, N_EPISODES)
alphas = []
for i in range(N_EPISODES):
    alphas.append((1.0 - MIN_ALPHA) * (1 - (i / N_EPISODES)) + MIN_ALPHA)
gamma = 1.0
eps = 0.2

q_table = dict()


def q(state, action=None):
    if state not in q_table:
        print("TEST:")
        print(state)
        print("q_table:")
        for s in q_table:
            print(s)
        #q_table[state] = np.zeros(len(ACTIONS))
        zeros = []
        for i in range(len(ACTIONS)):
            zeros.append(0)
        q_table[state] = zeros

    if action is None:
        return q_table[state]

    return q_table[state][action]

def choose_action(state):
    if random.uniform(0, 1) < eps:
        return random.choice(ACTIONS)
    else:
        #return np.argmax(q(state))
        return q(state).index(max(q(state)))


for e in range(N_EPISODES):

    state = start_state
    total_reward = 0
    alpha = alphas[e]

    for _ in range(MAX_EPISODE_STEPS):
        action = choose_action(state)
        next_state, reward, done = act(state, action)
        total_reward += reward

        """q(state)[action] = q(state, action) + \
                           alpha * (reward + gamma * np.max(q(next_state)) - q(state, action))"""
        q(state)[action] = q(state, action) + \
                           alpha * (reward + gamma * max(q(next_state)) - q(state, action))
        state = next_state
        if done:
            break
    print(f"Episode {e + 1}: total reward -> {total_reward}")

