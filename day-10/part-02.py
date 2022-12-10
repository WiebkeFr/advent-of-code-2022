def draw(current_cycle, x):
    if (current_cycle - 1) % 40 in [x - 1, x, x + 1]:
        print("#", end="")
    else:
        print(".", end="")


def start_cycle(current_cycle, x):
    cycles = range(40, 251, 40)
    if current_cycle in cycles:
        results.append(current_cycle * x)
        print("")


with open("input.txt", "r") as file:
    steps = file.read().split("\n")
    results = []
    x = 1
    current_cycle = 0

    for step in steps:
        current_cycle += 1
        draw(current_cycle, x)
        start_cycle(current_cycle, x)

        if step != "noop":
            current_cycle += 1
            draw(current_cycle, x)
            start_cycle(current_cycle, x)

            _, number = step.split(" ")
            x += int(number)
