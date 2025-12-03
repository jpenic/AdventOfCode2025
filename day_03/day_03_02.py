with open('input.txt', 'r') as f:
    lines = f.read().split()

def get_max_joltage(battery_bank, num_of_digits_needed):
    if num_of_digits_needed == 0:
        return ''
    max_digit = max(battery_bank)
    max_digit_idx = battery_bank.index(max_digit)
    if len(battery_bank) - max_digit_idx >= num_of_digits_needed:
        # if there are enough digits after the max digit, find the largest possible number in the
        # rest of the string
        return max_digit + get_max_joltage(battery_bank[max_digit_idx + 1:], num_of_digits_needed - 1)
    else:
        # if there aren't enough digits after the max digit, find the next largest digit in front of it, and then
        # find the largest possible number in the rest of the string
        tmp_battery_bank = battery_bank.replace(max_digit, '0')
        while len(battery_bank) - max_digit_idx < num_of_digits_needed:
            max_digit = max(tmp_battery_bank)
            max_digit_idx = battery_bank.index(max_digit)
            tmp_battery_bank = tmp_battery_bank.replace(max_digit, '0')
        return max_digit + get_max_joltage(battery_bank[max_digit_idx + 1:], num_of_digits_needed - 1)


total_sum = 0

for line in lines:
    battery_bank = line.strip()
    total_sum += int(get_max_joltage(battery_bank, 12))

print('Result:', total_sum)