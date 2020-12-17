with open('input') as f:
    lines = [line for line in f.read().strip().split()]


# Part 1
def parse_v1(lines):
    active = set()
    for y, line in enumerate(lines):
        for x, state in enumerate(line):
            if state == '#':
                active.add((x, y, 0))
    return active


def neighbors_v1(x, y, z):
    for d_x in range(-1, 2):
        for d_y in range(-1, 2):
            for d_z in range(-1, 2):
                if not (d_x == d_y == d_z == 0):
                    yield (x + d_x, y + d_y, z + d_z)


def run_v1(state):
    def iteration():
        next_state = set()
        to_eval = set()
        for x, y, z in state:
            to_eval.update(neighbors_v1(x, y, z))
        for x, y, z in to_eval:
            n = len(state & set(neighbors_v1(x, y, z)))
            if (x, y, z) in state:
                if n in (2, 3):
                    next_state.add((x, y, z))
            else:
                if n == 3:
                    next_state.add((x, y, z))
        return next_state
    for i in range(6):
        state = iteration()
    print(len(state))


# Part 2
def parse_v2(lines):
    active = set()
    for y, line in enumerate(lines):
        for x, state in enumerate(line):
            if state == '#':
                active.add((x, y, 0, 0))
    return active


def neighbors_v2(x, y, z, w):
    for d_x in range(-1, 2):
        for d_y in range(-1, 2):
            for d_z in range(-1, 2):
                for d_w in range(-1, 2):
                    if not (d_x == d_y == d_z == d_w == 0):
                        yield (x + d_x, y + d_y, z + d_z, w + d_w)


def run_v2(state):
    def iteration():
        next_state = set()
        to_eval = set()
        for x, y, z, w in state:
            to_eval.update(neighbors_v2(x, y, z, w))
        for x, y, z, w in to_eval:
            n = len(state & set(neighbors_v2(x, y, z, w)))
            if (x, y, z, w) in state:
                if n in (2, 3):
                    next_state.add((x, y, z, w))
            else:
                if n == 3:
                    next_state.add((x, y, z, w))
        return next_state
    for i in range(6):
        state = iteration()
    print(len(state))
