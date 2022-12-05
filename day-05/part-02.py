def do_procedure(crates, procedure):
    _, num, _, from_i, _, to_i = procedure.split(" ")
    crates_to_move = []
    for n in range(int(num)):
        element = crates[int(from_i) - 1].pop()
        crates_to_move.append(element)
    crates[int(to_i) - 1] += reversed(crates_to_move)


def initialize(state):
    state_as_list = state.split("\n")
    max_index = state_as_list.pop()[-1]
    state_as_list = list(reversed(state_as_list))
    stacked = []
    for i in range(int(max_index)):
        row = []
        for state_row in state_as_list:
            element = state_row[:3]
            if len(element.replace(" ", "")) > 0:
                row.append(state_row[:3])

        for j in range(int(len(state_as_list))):
            state_as_list[j] = state_as_list[j][3:]
            if len(state_as_list[j]) > 0:
                state_as_list[j] = state_as_list[j][1:]
        stacked.append(row)
    return stacked


with open("input.txt", "r") as input:
    state, stack = input.read().split("\n\n")
    crates = initialize(state)
    for procedure in stack.split("\n"):
        do_procedure(crates, procedure)
    result = [column[-1] for column in crates]
    print(result)

