with open('input.txt', 'r') as f:
    lines = f.read().split()

range_list = []
collecting_ranges = True
fresh_counter = 0
for line in lines:
    if collecting_ranges:
        if '-' not in line:
            collecting_ranges = False
            break
        start = int(line.strip().split('-')[0])
        end = int(line.strip().split('-')[1])
        range_list.append([start, end])

def fix_overlaps(ranges):
    ranges.sort(key = lambda x: x[0])
    new_ranges = [ranges[0]]
    for i in range(1, len(ranges)):
        current_range = new_ranges[-1]
        if ranges[i][0] <= current_range[1]:
            if ranges[i][1] >= current_range[1]:
                current_range[1] = ranges[i][1]
        else:
            new_ranges.append(ranges[i])
    return new_ranges

range_list.sort(key = lambda x: x[0])
fresh_ranges = [range_list[0]]
for start, end in range_list:
    add_to_the_end = True
    for fr in fresh_ranges:
        if fr[0] <= start <= fr[1] <= end:
            fr[1] = end
            add_to_the_end = False
    if add_to_the_end:
        fresh_ranges.append([start, end])

    fresh_ranges = fix_overlaps(fresh_ranges)

print(fresh_ranges)

result = 0
for fr in fresh_ranges:
    result += fr[1] - fr[0] + 1

print("Result:", result)