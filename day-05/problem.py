from collections import Counter

translation = str.maketrans('FBLR', '0101')

with open('input') as f:
    records = [(int(line[:7].translate(translation), 2), int(line[7:].translate(translation), 2)) for line in f.read().strip().split()]

# Part 1
max_seat_id = 0
for row, seat in records:
    max_seat_id = max(max_seat_id, row * 8 + seat)

print(max_seat_id)

# Part 2
c = Counter([row for row, _ in records])
my_row = [k for k, v in c.items() if v == 7][0]
my_seat = list(set(range(8)) - set([seat for row, seat in records if row == my_row]))[0]
print(my_row * 8 + my_seat)
