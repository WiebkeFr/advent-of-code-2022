def is_overlapping(pair):
    separated_pairs = pair.split(",")
    first_interval = separated_pairs[0].split("-")
    second_interval = separated_pairs[1].split("-")
    if int(first_interval[0]) <= int(second_interval[0]) and int(second_interval[1]) <= int(first_interval[1]):
        return True
    if int(second_interval[0]) <= int(first_interval[0]) and int(first_interval[1]) <= int(second_interval[1]):
        return True
    return False


with open("input.txt", "r") as input:
    data = input.read().split("\n")
    overlapping_pairs = filter(is_overlapping, data)
    result = len(list(overlapping_pairs))
