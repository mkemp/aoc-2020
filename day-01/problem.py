from itertools import combinations

with open('input') as f:
    values = [int(line) for line in f.read().strip().split()]

# Part 1
for i, j in combinations(values, 2):
    if i + j == 2020:
        print(i * j)

# Part 2
for i, j, k in combinations(values, 3):
    if i + j + k == 2020:
        print(i * j * k)
