from functools import reduce

with open('input') as f:
    lines = [line for line in f.read().strip().split()]


# Part 1
timestamp = int(lines[0])
buses = [int(x) for x in lines[1].strip().split(',') if x != 'x']
delta_by_bus = {}
for bus in buses:
  delta_by_bus[bus - (timestamp % bus)] = bus
print(reduce(lambda a, b: a * b, sorted(delta_by_bus.items())[0]))


# Part 2
# from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(m_array, r_array):
    total = 0
    total_prod = reduce(lambda a, b: a * b, m_array)
    for m_val, r_val in zip(m_array, r_array):
        mod_prod = total_prod // m_val
        total += r_val * multiplicative_inverse(mod_prod, m_val) * mod_prod
    return total, total % total_prod


# from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def multiplicative_inverse(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


buses = [int(x) if x != 'x' else None for x in lines[1].strip().split(',')]
modulos = [bus for bus in buses if bus]
remainders = [-i % bus for i, bus in enumerate(buses) if bus]
print(chinese_remainder(modulos, remainders))
