with open("input.txt", "r") as file:
    steps = file.read().split("\n")
    cycles = range(20, 221, 40)
    results = []
    x = 1
    current_cycle = 0

    for step in steps:
        current_cycle += 1
        if current_cycle in cycles:
            results.append(current_cycle * x)

        if step != "noop":
            current_cycle += 1
            if current_cycle in cycles:
                results.append(current_cycle * x)

            _, number = step.split(" ")
            x += int(number)

    print(sum(results))