with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

numbers = []
for line in lines[:-1]:
    numbers.append(line)

operations = lines[-1].split()
results = []
new_numbers = []
new_number_list = []
for j in range(len(numbers[0])):
    new_number = ''
    for i in range(len(numbers)):
        new_number += numbers[i][j]
    try:
        new_number_list.append(int(new_number))
    except ValueError:
        # exception is thrown when the string contains only spaces, then the current list of numbers gets saved,
        # and the next set of numbers are parsed
        new_numbers.append(new_number_list)
        new_number_list = []

new_numbers.append(new_number_list)
result = 0
for i in range(len(new_numbers)):
    add_result = 0
    multiply_result = 1
    for j in range(len(new_numbers[i])):
        if operations[i] == '+':
            add_result += new_numbers[i][j]
        elif operations[i] == '*':
            multiply_result *= new_numbers[i][j]
    if operations[i] == '+':
        result += add_result
    elif operations[i] == '*':
        result += multiply_result

print("Result:", result)