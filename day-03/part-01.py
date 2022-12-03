def get_item(rucksack):
    split_index = int(len(rucksack)/2)
    first_container = rucksack[:split_index]
    second_container = rucksack[split_index:]
    element = set(first_container).intersection(second_container).pop()
    num = ord(element)
    if num > 96:
        return num - 96
    else:
        return num - 38


with open('input.txt', 'r') as input:
    data = input.read().split('\n')
    e = map(get_item, data)
    result = sum(e)

