
def color_index_to_pair_number(major_index, minor_index):
    return major_index * 5 + minor_index + 1

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{color_index_to_pair_number(i, j)} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)


result = print_color_map()
assert(color_index_to_pair_number(0, 0) == 1)
assert(color_index_to_pair_number(0, 1) == 2)
assert(color_index_to_pair_number(1, 0) == 6)
assert(color_index_to_pair_number(4, 4) == 25)
assert(result == 25)
print("All is well (maybe!)")
