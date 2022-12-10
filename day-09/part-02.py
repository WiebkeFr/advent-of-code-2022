def is_adjacent(h, t):
    return abs(h[0] - t[0]) < 2 and abs(h[1] - t[1]) < 2


def next_step(dir, head):
    if dir == "U":
        return head[0], head[1] + 1
    if dir == "R":
        return head[0] + 1, head[1]
    if dir == "D":
        return head[0], head[1] - 1
    if dir == "L":
        return head[0] - 1, head[1]


def compute_step(node, next_node):
    if is_adjacent(node, next_node):
        return next_node

    x = 1 if node[0] > next_node[0] else - 1
    y = 1 if node[1] > next_node[1] else - 1

    if node[1] == next_node[1]:
        return next_node[0] + x, next_node[1]

    if node[0] == next_node[0]:
        return next_node[0], next_node[1] + y
    return next_node[0] + x, next_node[1] + y


with open("input.txt", "r") as file:
    steps = file.read().split("\n")
    visited = [(0, 0)]
    nodes = [(0, 0) for _ in range(10)]

    for step in steps:
        direction, num = step.split(" ")

        for i in range(int(num)):
            nodes[0] = next_step(direction, nodes[0])
            for node_index in range(1, len(nodes)):
                nodes[node_index] = compute_step(nodes[node_index - 1], nodes[node_index])

            visited.append(nodes[-1])

    print(len(set(visited)))