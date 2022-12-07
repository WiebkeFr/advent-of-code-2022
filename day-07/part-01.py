class TreeNode:
    def __init__(self, name, size=None, parent=None):
        self.name = name
        self.size = size
        self.children = []
        self.parent = parent


def add_node(node_list, current_dir):
    while len(node_list) > 0 and "$" not in node_list[0]:
        node = node_list.pop(0)
        info, name = node.split(" ")
        size = None if "dir" in info else info
        new_node = TreeNode(name, size, current_dir)
        current_dir.children.append(new_node)


def initialize_tree(lines_list, current_dir):
    if len(lines_list) > 0:
        line = lines_list.pop(0)
        if "$" in line:
            if "$ ls" in line:
                add_node(lines_list, current_dir)
                initialize_tree(lines_list, current_dir)
            elif "cd" in line:
                _, _, dir_name = line.split(" ")
                if dir_name != "..":
                    current_node = list(filter(lambda x: x.name == dir_name, current_dir.children))[0]
                    initialize_tree(lines_list, current_node)
                else:
                    initialize_tree(lines_list, current_dir.parent)


def get_size(tree, current_size):
    if any(child.size is None for child in tree.children):
        for child in tree.children:
            if child.size is None:
                current_size = get_size(child, current_size)

    dir_size = sum(list(map(lambda x: int(x.size), tree.children)))
    tree.size = dir_size
    if dir_size <= 100000:
        current_size += dir_size

    return current_size


with open("input.txt", "r") as file:
    lines = file.read().split("\n")
    lines.pop(0)
    root = TreeNode("/")
    initialize_tree(lines, root)
    size = get_size(root, 0)
    print(size)
