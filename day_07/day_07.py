with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

split_counter = 0

start_position = lines[0].index('S')

curr_beam_idxs = [start_position]

for i in range(1, len(lines)):
    print("i", i)
    new_beam_idxs = []
    for idx in curr_beam_idxs:
        print("idx", idx)
        if lines[i][idx] == '^':
            split_counter += 1
            if idx - 1 >= 0 and idx - 1 not in new_beam_idxs:
                new_beam_idxs.append(idx - 1)
            if idx + 1 < len(lines[i]) and idx + 1 not in new_beam_idxs:
                new_beam_idxs.append(idx + 1)
        elif idx not in new_beam_idxs:
            new_beam_idxs.append(idx)
    curr_beam_idxs = new_beam_idxs

print("Result:", split_counter)