def compute_score(x):
    shapes = x.split(" ")
    score = 0
    if shapes[1] == "X":
        if shapes[0] == "A":
            score += 3
        if shapes[0] == "B":
            score += 1
        if shapes[0] == "C":
            score += 2
    if shapes[1] == "Y":
        score += 3
        if shapes[0] == "A":
            score += 1
        if shapes[0] == "B":
            score += 2
        if shapes[0] == "C":
            score += 3
    if shapes[1] == "Z":
        score += 6
        if shapes[0] == "A":
            score += 2
        if shapes[0] == "B":
            score += 3
        if shapes[0] == "C":
            score += 1
    return score


with open('input.txt', 'r') as input:
    data = input.read().split('\n')
    data = map(compute_score, data)
    result = sum(data)
