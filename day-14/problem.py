from collections import defaultdict
from itertools import zip_longest

with open('input') as f:
    lines = [line for line in f.read().strip().split('\n')]


# Part 1
class MemoryV1(object):
    def __init__(self):
        super(MemoryV1, self).__init__()
        self.mask_or, self.mask_and = [0] * 32, [1] * 32
        self.mem = defaultdict(lambda: 0)
    def do_mask(self, value):
        self.mask_or, self.mask_and = [0] * 32, [1] * 32
        for c in value:
            if c == '1':
                self.mask_or.append(1)
                self.mask_and.append(1)
            elif c == '0':
                self.mask_or.append(0)
                self.mask_and.append(0)
            else:  # X
                self.mask_or.append(0)
                self.mask_and.append(1)
    def do_mem(self, index, value):
        bits = [
            str(v & a | o)
            for v, o, a in zip_longest([int(x) for x in bin(value)[2:][::-1]], self.mask_or[::-1], self.mask_and[::-1], fillvalue=0)
        ][::-1]
        self.mem[index] = int('0b%s' % ''.join(bits), 2)


m = MemoryV1()
for line in lines:
    cmd, _, value = line.partition(' = ')
    if cmd == 'mask':
        m.do_mask(value)
    else:
        m.do_mem(int(cmd[4:-1]), int(value))

print(sum(m.mem.values()))

# Part 2
class MemoryV2(object):
    def __init__(self):
        super(MemoryV2, self).__init__()
        self.mask = 0
        self.mem = defaultdict(lambda: 0)
    def do_mask(self, value):
        self.mask = value
    def do_mem(self, index, value):
        for address in self.compute_addresses(index):
            self.mem[address] = value
    def compute_addresses(self, index):
        addresses = [[]]
        for m, i in zip_longest(self.mask[::-1], bin(index)[2:][::-1], fillvalue='0'):
            if m == '1':
                for a in addresses:
                    a.append('1')
            elif m == '0':
                for a in addresses:
                    a.append(i)
            else:
                copy = [a[:] + ['1'] for a in addresses]
                for a in addresses:
                    a.append('0')
                addresses.extend(copy)
        return [int('0b%s' % ''.join(a[::-1]), 2) for a in addresses]


m = MemoryV2()
for line in lines:
    cmd, _, value = line.partition(' = ')
    if cmd == 'mask':
        m.do_mask(value)
    else:
        m.do_mem(int(cmd[4:-1]), int(value))

print(sum(m.mem.values()))

