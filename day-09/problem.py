from itertools import combinations

with open('input') as f:
    lines = [int(line) for line in f.read().strip().split()]

# Part 1
for index, line in enumerate(lines[25:], 25):
    if not any(map(lambda x: sum(x) == line, combinations(lines[index-25:index], 2))):
        print(f'{index} : {line}')
        break

# Part 2
limit = 508
candidates = lines[:limit]
for index in range(0, limit - 2):
    for num in range(2, limit - index):
        c = lines[index:index + num]
        if sum(c) == lines[limit]:
            print(min(c) + max(c))
            break
