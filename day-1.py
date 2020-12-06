input_filename = 'input/day1_input.txt'
with open(input_filename) as input_file:
    numbers = [int(number.rstrip()) for number in input_file]

for i in range(0, len(numbers)):
    for j in range(0, len(numbers)):
        if numbers[i] + numbers[j] == 2020 and i != j:
            print(f'part 1 answer: {numbers[i] * numbers[j]}')
        for k in range(0, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k]== 2020 and i != j and j != k:
                print(f'part 2 answer: {numbers[i] * numbers[j] * numbers[k]}')

