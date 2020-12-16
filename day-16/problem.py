with open('input') as f:
    lines = [line for line in f.read().strip().split('\n')]


validations = {
    'departure_location': lambda x: 29 <= x <= 917 or 943 <= x <= 952,
    'departure_station': lambda x: 50 <= x <= 875 or 884 <= x <= 954,
    'departure_platform': lambda x: 41 <= x <= 493 or 503 <= x <= 949,
    'departure_track': lambda x: 50 <= x <= 867 or 875 <= x <= 966,
    'departure_date': lambda x: 30 <= x <= 655 or 679 <= x <= 956,
    'departure_time': lambda x: 46 <= x <= 147 or 153 <= x <= 958,
    'arrival_location': lambda x: 50 <= x <= 329 or 344 <= x <= 968,
    'arrival_station': lambda x: 42 <= x <= 614 or 623 <= x <= 949,
    'arrival_platform': lambda x: 35 <= x <= 849 or 860 <= x <= 973,
    'arrival_track': lambda x: 42 <= x <= 202 or 214 <= x <= 959,
    'class': lambda x: 38 <= x <= 317 or 329 <= x <= 968,
    'duration': lambda x: 44 <= x <= 530 or 539 <= x <= 953,
    'price': lambda x: 28 <= x <= 713 or 727 <= x <= 957,
    'route': lambda x: 30 <= x <= 157 or 179 <= x <= 966,
    'row': lambda x: 38 <= x <= 114 or 136 <= x <= 969,
    'seat': lambda x: 45 <= x <= 441 or 465 <= x <= 956,
    'train': lambda x: 44 <= x <= 799 or 824 <= x <= 951,
    'type': lambda x: 41 <= x <= 411 or 437 <= x <= 953,
    'wagon': lambda x: 39 <= x <= 79 or 86 <= x <= 969,
    'zone': lambda x: 48 <= x <= 306 or 317 <= x <= 974,
}

my_record = [int(value) for value in lines[lines.index('your ticket:') + 1].split(',')]
records = [[int(value) for value in line.split(',')] for line in lines[lines.index('nearby tickets:') + 1:]]

# Part 1
ticket_scanning_error_rate = 0
for record in records:
    for value in record:
        if not any([validation(value) for validation in validations.values()]):
            ticket_scanning_error_rate += value

print(ticket_scanning_error_rate)

# Part 2
valid_records = [my_record]
for record in records:
    valid = True
    for value in record:
        if not any([validation(value) for validation in validations.values()]):
            valid = False
            break
    if valid:
        valid_records.append(record)

matches = {}
for i in range(len(my_record)):
    labels = set()
    for label, validation in validations.items():
        if all(validation(record[i]) for record in valid_records):
            labels.add(label)
    matches[i] = labels

resolved = {}
for _ in range(len(matches)):
    for i, labels in [(i, labels) for (i, labels) in matches.items() if len(labels) == 1]:
        resolved[i] = list(labels)[0]
        for j in matches:
            if j != i:
                matches[j] -= labels

departure_fields = [key for key, val in resolved.items() if val.startswith('departure')]
result = 1
for i in departure_fields:
    result *= my_record[i]

print(result)
