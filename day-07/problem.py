from collections import defaultdict


def build_mapping_from_input():
    forward, reverse = defaultdict(dict), defaultdict(dict)
    with open('input') as f:
        for line in f.read().strip().split('\n'):
            container, _, subcontainers = line[:-1].partition(' bags contain ')
            for token in subcontainers.replace(' bags', '').replace(' bag', '').split(', '):
                if token != 'no other':
                    count, _, subcontainer = token.partition(' ')
                    forward[container][subcontainer] = int(count)
                    reverse[subcontainer][container] = int(count)
    return forward, reverse


forward, reverse = build_mapping_from_input()


# Part 1
def can_contain(subcontainer, seen=None):
    seen = seen or set()
    for container in reverse[subcontainer]:
        if container not in seen:
            seen.add(container)
            can_contain(container, seen)
    return seen


print(len(can_contain('shiny gold')))


# Part 2
def count_bags(container):
    total = 0
    subcontainers = forward.get(container, {})
    for subcontainer, count in subcontainers.items():
        total += count * (1 + count_bags(subcontainer))
    return total


print(count_bags('shiny gold'))
