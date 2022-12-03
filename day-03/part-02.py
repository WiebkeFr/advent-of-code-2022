def compute_priorities(rucksack):
    element = set(rucksack[0]) & set(rucksack[1]) & set(rucksack[2])
    num = ord(element.pop())
    if num > 96:
        return num - 96
    else:
        return num - 38


with open('input.txt', 'r') as input:
    data = input.read().split('\n')
    number_of_groups = int(len(data)/3)
    grouped_data = [data[i*3:i*3+3] for i in range(number_of_groups)]
    result = map(compute_priorities, grouped_data)
