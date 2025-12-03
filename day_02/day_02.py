from math import ceil

with open('input.txt', 'r') as f:
    lines = f.read().split()

ranges_input = []
for line in lines:
    ranges_input.extend(line.split(','))

ranges = []
for r in ranges_input:
    if len(r) == 0:
        continue
    ranges.append(r.split('-'))


def sum_of_invalid_ids(start, end):
    total = 0
    # if the start and end range have an odd number of digits, and are the same length, there aren't any invalid IDs
    if len(start) % 2 == 1 and len(end) % 2 == 1 and len(start) == len(end):
        return 0
    start_len = len(start) // 2
    end_len = ceil(len(end) / 2)
    start_digits = start[:start_len]
    if len(start_digits) == 0:
        start_digits = 0
    else:
        start_digits = int(start_digits)

    end_digits = int(end[:end_len])

    for i in range(start_digits, end_digits + 1):
        id = int(str(i) + str(i))
        if int(start) <= id <= int(end):
            total += id

    return total

total_sum = 0
for r in ranges:
    total_sum += sum_of_invalid_ids(r[0], r[1])

print("Result:", total_sum)
