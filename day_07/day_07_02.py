with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

start_position = lines[0].index('S')
curr_beam_idxs = {start_position: 1}
# active beam column index and the number of beams in that position
# (all overlapping beams from different timelines are counted)

# iterating through all possible beams (in each row), finding indexes for the next row (depending on splitters)
# and keeping count of all the overlapping beams
for i in range(1, len(lines)):
    print("Row:", i)
    new_beam_idxs = {}
    for idx in curr_beam_idxs:
        if lines[i][idx] == '^':
            if idx - 1 >= 0:
                if idx - 1 in new_beam_idxs:
                    curr_count = new_beam_idxs.get(idx - 1)
                else:
                    curr_count = 0
                new_beam_idxs.update({idx - 1: curr_beam_idxs[idx] + curr_count})
            if idx + 1 < len(lines[i]):
                if idx + 1 in new_beam_idxs:
                    curr_count = new_beam_idxs.get(idx + 1)
                else:
                    curr_count = 0
                new_beam_idxs.update({idx + 1: curr_beam_idxs[idx] + curr_count})
        else:
            if idx in new_beam_idxs:
                curr_count = new_beam_idxs.get(idx)
            else:
                curr_count = 0
            new_beam_idxs.update({idx: curr_beam_idxs[idx] + curr_count})
    curr_beam_idxs = new_beam_idxs


# the result is the sum of all overlapping beams in the last row of the map
result = 0
for idx in curr_beam_idxs:
    result += curr_beam_idxs[idx]
print("Result:", result)
