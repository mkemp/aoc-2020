from collections import defaultdict

with open('input') as f:
    values = sorted([int(line) for line in f.read().strip().split()], reverse=True)
    values = [values[0] + 3] + values + [0]

# Part 1
deltas = defaultdict(int)
prior_value = values[0]
for value in values[1:]:
    deltas[abs(prior_value - value)] += 1
    prior_value = value

print(deltas[1] * deltas[3])


# Part 2
def find_chains(values):
    chains = []
    current_chain = []
    prior_value = values[0]
    for value in values[1:]:
        if abs(prior_value - value) < 3:
            current_chain.append(value)
        else:
            if len(current_chain) > 1:
                chains.append(current_chain)
            current_chain = [value]
        prior_value = value
    chains.append(current_chain)
    return chains


perms = 1
for chain in find_chains(values):
    perms *= {
        2: 1,
        3: 2,
        4: 4,
        5: 7
    }[len(chain)]

print(perms)


def solve(path, remaining_values):
    found = 0
    if len(remaining_values) <= 1:
        found = 1
    else:
        for i, value in enumerate(remaining_values[:3]):
            if path[-1] <= value + 3:
                found += solve(path + [value], remaining_values[i + 1:])
    return found


print(solve([4], [3]))           # -> 1
print(solve([4], [3, 2]))        # -> 2
print(solve([4], [3, 2, 1]))     # -> 4
print(solve([4], [3, 2, 1, 0]))  # -> 7
