from collections import Counter

with open('input') as f:
    lines = f.read().strip().split()

rows, cols = len(lines), len(lines[0])
deltas = (
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1)
)


# Part 1
def occupied_v1(state, row, col):
    visible = 0
    for (d_x, d_y) in deltas:
        x, y = row, col
        if x + d_x not in (-1, rows) and y + d_y not in (-1, cols):
            visible += 1 if state[x + d_x][y + d_y] == '#' else 0
    return visible


def iteration(state, occupied, occupied_threshold=4):
    new_state = []
    for row in range(rows):
        chars = []
        for col in range(cols):
            val = state[row][col]
            if val != '.':
                occ = occupied(state, row, col)
                if val == 'L' and occ == 0:
                    val = '#'
                elif val == '#' and occ >= occupied_threshold:
                    val = 'L'
            chars.append(val)
        new_state.append(''.join(chars))
    return new_state


def find_occupied(state):
    c = Counter()
    for row in state:
        c.update(row)
    return c['#']


last_state, state = None, iteration(lines, occupied_v1)
while state != last_state:
    last_state, state = state, iteration(state, occupied_v1)

print(find_occupied(state))


# Part 2
def occupied_v2(state, row, col):
    visible = 0
    for (d_x, d_y) in deltas:
        x, y = row, col
        while x + d_x not in (-1, rows) and y + d_y not in (-1, cols):
            x, y = x + d_x, y + d_y
            val = state[x][y]
            if val != '.':
                if val == '#':
                    visible += 1
                break
    return visible


last_state, state = None, iteration(lines, occupied_v2, 5)
while state != last_state:
    last_state, state = state, iteration(state, occupied_v2, 5)

print(find_occupied(state))
