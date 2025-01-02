import copy

FILENAME = ["input.txt", "testInput.txt"]

dirs = {
    'top': (0, -1),
    'bottom': (0, 1),
    'left': (-1, 0),
    'right': (1, 0)
}


def read_file() -> list[list[str]]:
    with open(FILENAME[0], 'r') as file:
        return [[x for x in line.strip("\n")] for line in file]


def find_starting_spot(grid: list[list[str]]) -> tuple[int, int]:
    for y, row in enumerate(grid):
        if "^" in row:
            return (row.index("^"), y)


def find_all_visited_nodes(grid: list[list[str]], starting_pos: tuple[int, int]) -> set[tuple[int, int]]:
    current_direction = 'top'
    visited_pos = set()

    while True:
        next_field = (starting_pos[0] + dirs[current_direction][0],
                      starting_pos[1] + dirs[current_direction][1])

        if next_field[0] < 0 or next_field[0] >= len(grid[0]) or next_field[1] < 0 or next_field[1] >= len(grid):
            break

        if grid[next_field[1]][next_field[0]] == "#":
            current_direction = change_direction(current_direction)
            continue

        starting_pos = (next_field[0], next_field[1])

        visited_pos.add(starting_pos)

    return visited_pos


def check_if_map_contains_loop(grid: list[list[str]], starting_position: tuple[int, int], max_count: int) -> bool:
    current_direction = 'top'
    visited_in_curr_iteration = set()
    count = 0
    while count < max_count:

        next_field = (starting_position[0] + dirs[current_direction][0],
                      starting_position[1] + dirs[current_direction][1])

        if next_field[0] < 0 or next_field[0] >= len(grid[0]) or next_field[1] < 0 or next_field[1] >= len(grid):
            break

        if grid[next_field[1]][next_field[0]] == "#":
            current_direction = change_direction(current_direction)
            continue

        starting_position = (next_field[0], next_field[1])

        if (starting_position[0], starting_position[1], current_direction) in visited_in_curr_iteration:
            return True

        visited_in_curr_iteration.add((starting_position[0], starting_position[1], current_direction))
        count += 1

    return False


def change_direction(current_direction: str) -> str:
    ret = ""
    if current_direction == 'top':
        ret = 'right'
    elif current_direction == 'right':
        ret = 'bottom'
    elif current_direction == 'bottom':
        ret = 'left'
    elif current_direction == 'left':
        ret = "top"
    return ret


def part1() -> int:
    input_list = read_file()
    starting_pos = find_starting_spot(input_list)
    return len(find_all_visited_nodes(input_list, starting_pos))


def part2() -> int:  # takes some time
    input_list = read_file()
    starting_pos = find_starting_spot(input_list)
    visited_pos = find_all_visited_nodes(input_list, starting_pos)

    clean_map = copy.deepcopy(input_list)
    loops = 0
    for obstacle in list(visited_pos):
        input_list = copy.deepcopy(clean_map)
        new_obstacle = (obstacle[0], obstacle[1])
        input_list[new_obstacle[1]][new_obstacle[0]] = '#'

        starting_position = (starting_pos[0], starting_pos[1])
        loops += check_if_map_contains_loop(input_list, starting_position, len(visited_pos)*2)
    return loops


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
