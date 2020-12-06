from functools import reduce
from operator import and_

# Part 1
with open('input') as f:
    records = [set(line.replace('\n', '')) for line in f.read().strip().split('\n\n')]

print(sum(map(len, records)))

# Part 2
with open('input') as f:
    records = [reduce(and_, (set(token) for token in line.split())) for line in f.read().strip().split('\n\n')]

print(sum(map(len, records)))
