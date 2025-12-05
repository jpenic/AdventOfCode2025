with open('input.txt', 'r') as f:
    lines = f.read().split()

def check_freshness(ranges, ingredient_id):
    for r in ranges:
        if r[0] <= ingredient_id <= r[1]:
            return True
    return False


range_list = []
collecting_ranges = True
fresh_counter = 0
for line in lines:
    if collecting_ranges:
        if '-' not in line:
            collecting_ranges = False
            continue
        start = int(line.strip().split('-')[0])
        end = int(line.strip().split('-')[1])
        range_list.append((start, end))
    else:
        fresh_counter += check_freshness(range_list, int(line.strip()))

print("Result:", fresh_counter)