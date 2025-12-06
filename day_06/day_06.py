with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

numbers = []
for line in lines[:-1]:
    numbers.append(line.split())

operations = lines[-1].split()
results = []
for j in range(len(numbers[0])):
    add_result = 0
    multiply_result = 1
    for i in range(len(numbers)):
        if operations[j] == '+':
            add_result += int(numbers[i][j])
        elif operations[j] == '*':
            multiply_result *= int(numbers[i][j])
    if operations[j] == '+':
        results.append(add_result)
    elif operations[j] == '*':
        results.append(multiply_result)

result = sum(results)
print("Result:", result)