with open('input.txt', 'r') as f:
    lines = f.read().split()

list_counter = [0] * 100
list_pointer = 50
for line in lines:
    direction = line[0]
    if direction == 'L':
        step = -1
    else:
        step = 1
    distance = int(line[1:])
    for i in range(0, distance):
        list_pointer += step
        list_pointer = list_pointer % 100
        list_counter[list_pointer] += 1
print(list_counter)
print("Result:", list_counter[0])
