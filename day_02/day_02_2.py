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
    invalid_ids = set()

    max_repeat_digits = 10 ** (len(end) // 2)

    for repeat_digits in range(1, max_repeat_digits):
        if int(2 * str(repeat_digits)) > int(end):
            break

        num_of_reps_min = len(start) // len(str(repeat_digits))
        num_of_reps_max = len(end) // len(str(repeat_digits))

        for rep in range(num_of_reps_min, num_of_reps_max + 1):
            if int(start) <= int(rep * str(repeat_digits)) <= int(end):
                print("Invalid ID:", int(rep * str(repeat_digits)))
                invalid_ids.add(int(rep * str(repeat_digits)))
    return sum(invalid_ids)

total_sum = 0
for r in ranges:
    total_sum += sum_of_invalid_ids(r[0], r[1])

print("Result:", total_sum)
