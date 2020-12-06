with open('input') as f:
    lines = f.read().strip().split()


def count_trees(lines, right=1, down=1):
    idx = 0
    trees = 0
    for line in lines[down::down]:
        idx = (idx + right) % len(line)
        if line[idx] == '#':
            trees += 1
    return trees


# Part 1
print(count_trees(lines, 3))

# Part 2
print(count_trees(lines) * count_trees(lines, 3) * count_trees(lines, 5)  * count_trees(lines, 7) * count_trees(lines, down=2))
