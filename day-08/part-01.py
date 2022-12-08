import numpy as np

with open("input.txt", "r") as file:
    tree_rows = file.read().split("\n")
    tree_rows = [list(row) for row in tree_rows]
    transposed_rows = np.array(tree_rows).transpose()

    counter = 0
    for i, row in enumerate(tree_rows):
        for j, tree in enumerate(row):
            if i == 0 or j == 0 or i == len(tree_rows) or j == len(row):
                counter += 1
            elif all(x < tree for x in row[:j]) or all(x < tree for x in row[j+1:]):
                counter += 1
            elif all(x < tree for x in transposed_rows[j][:i]) or all(x < tree for x in transposed_rows[j][i+1:]):
                counter += 1
    print(counter)
