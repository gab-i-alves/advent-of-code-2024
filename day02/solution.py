
def is_safe_sequence(numbers):
    if numbers[0] > numbers[1]:
        is_descending = True
    else:
        is_descending = False

    diff = abs(numbers[0] - numbers[1])
    if diff < 1 or diff > 3:
        return False

    for i in range(1, len(numbers)-1):
        if is_descending:
            if numbers[i] < numbers[i+1]:
                return False
        else:
            if numbers[i] > numbers[i+1]:
                return False

        diff = abs(numbers[i] - numbers[i+1])
        if diff < 1 or diff > 3:
            return False
        
    return True


with open('day02/input.txt', 'r') as file:
    sequences = [list(map(int, line.split())) for line in file]
    counter = 0
    for sequence in sequences:
        passed = is_safe_sequence(sequence)
        if passed:
            counter += 1
    
    print(counter)
