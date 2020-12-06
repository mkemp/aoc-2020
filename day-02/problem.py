from collections import Counter
import re

line_re = re.compile('^(?P<min>\\d+)[-](?P<max>\\d+) (?P<letter>[a-z]): (?P<pw>[a-z]+)$')

with open('input') as f:
    parsed = [
        (int(m.group('min')), int(m.group('max')), m.group('letter'), m.group('pw'))
        for m in (line_re.match(line) for line in f.read().strip().split('\n'))
    ]

# Part 1
matches = 0
for i, j, letter, pw in parsed:
    if i <= Counter(pw).get(letter, 0) <= j:
        matches += 1
print(matches)

# Part 2
matches = 0
for i, j, letter, pw in parsed:
    if (pw[i - 1] == letter) != (pw[j - 1] == letter):
        matches += 1
print(matches)
