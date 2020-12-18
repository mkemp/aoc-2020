import re

with open('input') as f:
    lines = [line for line in f.read().strip().split('\n')]


# Part 1
class IntV1(object):

    def __init__(self, value):
        super(IntV1, self).__init__()
        self.value = value

    def __sub__(self, o):
        return IntV1(self.value * o.value)

    def __add__(self, o):
        return IntV1(self.value + o.value)


total = 0
for line in lines:
    total += eval(re.sub(r'(\d+)', r'IntV1(\1)', line.replace('*', '-'))).value

print(total)


# Part 2
class IntV2(object):

    def __init__(self, value):
        super(IntV2, self).__init__()
        self.value = value

    def __mul__(self, o):
        return IntV2(self.value + o.value)

    def __add__(self, o):
        return IntV2(self.value * o.value)


total = 0
for line in lines:
    total += eval(re.sub(r'(\d+)', r'IntV2(\1)', line.translate(str.maketrans('*+', '+*')))).value

print(total)
