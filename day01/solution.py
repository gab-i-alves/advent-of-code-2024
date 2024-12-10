
left_list = []
right_list = []
pairs = []
difs = []

INPUT = "/home/mars/Projects/advent-of-code-2024/day01/input.txt"

# 1. Open the input.txt and for each line separate both numbers based on the spaces between then
with open(INPUT, "r") as file:
    for line in file:
        left_ele, right_ele = line.split("   ")

        left_list.append(int(left_ele.removesuffix("\n")))
        right_list.append(int(right_ele.removesuffix("\n")))
        

# 2. Order both lists in ascending order
left_list.sort()
right_list.sort()
    
# print(f"L: {left_list} R: {right_list}")

# 3. Pair then up once ordered
# 4. Calculate the differences between each pair and store on a list
for i in range(len(left_list)):
    pair = [left_list[i], right_list[i]]
    pairs.append(pair)
    dif = abs(pair[0] - pair[1])
    # print(f"{pair[0]} - {pair[1]} = {dif}")
    difs.append(dif)

# 5. Sum all the elements of this last list
print(f"Part 1: {sum(difs)}")

####################### Part 2
# Take each number from the left list
# Count how many times it appears in the right list
# Multiply the left number by its frequency in the right list
# Sum all these products

elements = []

for n in left_list:
    frequency = right_list.count(n)
    mult = n * frequency
    elements.append(mult)

print(f"Part 2: {sum(elements)}")