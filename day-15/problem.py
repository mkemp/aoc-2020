from collections import defaultdict

with open('input') as f:
    lines = [line for line in f.read().strip().split('\n')]

values = [int(v) for v in lines[0].split(',')]


# Part 1
def seq(values, limit=2020):
    last_number, last_seen = 0, defaultdict(list)
    for i, v in enumerate(values):
        last_number = v
        last_seen[v].append(i)

    for i in range(len(values), limit):
        if len(last_seen[last_number]) == 1:
            last_number = 0
            last_seen[0].append(i)
        else:
            seen = last_seen[last_number]
            last_number = seen[-1] - seen[-2]
            last_seen[last_number].append(i)

    print(last_number)


seq(values)

# Part 2

seq(values, 30000000)
