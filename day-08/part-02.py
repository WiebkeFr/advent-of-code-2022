import numpy as np

with open("input.txt", "r") as file:
    tree_rows = file.read().split("\n")
    tree_rows = [list(row) for row in tree_rows]
    transposed_rows = np.array(tree_rows).transpose()

    max_counter = 0
    for i, row in enumerate(tree_rows):
        for j, tree in enumerate(row):
            if not(i == 0 or j == 0 or i == len(tree_rows) - 1 or j == len(row) - 1):
                tree_score = 1

                right = next((i for i, x in enumerate(row[j+1:]) if x >= tree), len(row[j+1:]) - 1)
                tree_score *= right + 1

                left = next((i for i, x in enumerate(row[:j][::-1]) if x >= tree), len(row[:j]) - 1)
                tree_score *= left + 1

                top = next((i for i, x in enumerate(transposed_rows[j][:i][::-1]) if x >= tree),
                           len(transposed_rows[j][:i]) - 1)
                tree_score *= top + 1

                down = next((i for i, x in enumerate(transposed_rows[j][i + 1:]) if x >= tree),
                            len(transposed_rows[j][i+1:]) - 1)
                tree_score *= down + 1

                max_counter = tree_score if tree_score > max_counter else max_counter

    print(max_counter)
