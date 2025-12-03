with open('input.txt', 'r') as f:
    lines = f.read().split()

def get_max_joltage(battery_bank):
    max_digit = max(battery_bank)
    max_digit_counter = battery_bank.count(max_digit)
    # if there is only one max digit, the largest number will be by adding the next largest digit in the rest of
    # the string
    if max_digit_counter == 1:
        max_digit_idx = battery_bank.index(max_digit)
        if max_digit_idx == len(battery_bank) - 1:
            second_digit = max(battery_bank[:max_digit_idx])
            return int(second_digit + max_digit)
        else:
            second_digit = max(battery_bank[max_digit_idx + 1:])
            return int(max_digit + second_digit)
    # if the max digit occurs more than once, the largest number is the max digit repeated twice
    else:
        return int(max_digit + max_digit)


total_sum = 0

for line in lines:
    battery_bank = line.strip()
    total_sum += get_max_joltage(battery_bank)

print('Result:', total_sum)