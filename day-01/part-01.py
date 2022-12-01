with open('input.txt', 'r') as input:
    data = input.read().split('\n\n')
    data = [sum(map(lambda x: int(x), calories.split("\n"))) for calories in data]
    result = max(data)