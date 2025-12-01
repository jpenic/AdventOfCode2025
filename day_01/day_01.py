with open('input.txt', 'r') as f:
    lines = f.read().split()

counter = 0
curr_value = 50
for line in lines:
    if line[0] == 'R':
        curr_value += int(line[1:])
    else:
        curr_value -= int(line[1:])
    curr_value = curr_value % 100
    if curr_value == 0:
        counter += 1

print("Result:", counter)
