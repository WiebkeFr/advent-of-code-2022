def compute_score(x):
    shapes = x.split(" ")
    score = 0
    if shapes[1] == "X":
        score += 1
        if shapes[0] == "A":
            score += 3
        if shapes[0] == "C":
            score += 6
    if shapes[1] == "Y":
        score += 2
        if shapes[0] == "B":
            score += 3
        if shapes[0] == "A":
            score += 6
    if shapes[1] == "Z":
        score += 3
        if shapes[0] == "C":
            score += 3
        if shapes[0] == "B":
            score += 6
    return score


with open('input.txt', 'r') as input:
    data = input.read().split('\n')
    data = map(compute_score, data)
    result = sum(data)
