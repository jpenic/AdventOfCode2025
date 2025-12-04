with open('input.txt', 'r') as f:
    lines = f.read().split()

grid_dict = {}

# using complex numbers for the grid coordinates
for row in range(len(lines)):
    for column in range(len(lines[row])):
        grid_dict[row * 1j + column] = lines[row][column]

movable_rolls = 0
at_least_one_roll_moved = True

while at_least_one_roll_moved:
    at_least_one_roll_moved = False
    positions = grid_dict.keys()
    for position in positions:
        if grid_dict.get(position) == '.':
            continue
        counter = 0
        for move in (1, -1, 1j, -1j,  1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j):
            if grid_dict.get(position + move) == '@':
                counter += 1
        if counter < 4:
            movable_rolls += 1
            at_least_one_roll_moved = True
            grid_dict[position] = '.'

print("Result:", movable_rolls)

