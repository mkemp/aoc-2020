import re

hgt_re = re.compile('^(?:1(?:[5678]\d|9[0-3])cm|(?:59|6\d|7[0-6])in)$')
hcl_re = re.compile('^#[0-9a-f]{6}$')
pid_re = re.compile('^\d{9}$')

rules = {
    'byr': lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    'iyr': lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    'eyr': lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    'hgt': lambda x: bool(hgt_re.match(x)),
    'hcl': lambda x: bool(hcl_re.match(x)),
    'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda x: bool(pid_re.match(x))
}
required = set(rules.keys())

with open('input') as f:
    records = [dict([token.split(':') for token in line.split()]) for line in f.read().strip().split('\n\n')]

# Part 1
valid = 0
for record in records:
    if required.issubset(set(record.keys())):
        valid += 1

print(valid)

# Part 2
valid = 0
for record in records:
    if required.issubset(set(record.keys())) and all(rule(record[key]) for key, rule in rules.items()):
        valid += 1

print(valid)
