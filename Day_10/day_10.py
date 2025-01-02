from collections import defaultdict

FILENAME = ["input.txt", "testInput.txt", "testInput2.txt"]

directions = {
    'bottom': (0, 1),
    'top': (0, -1),
    'right': (1, 0),
    'left': (-1, 0),
}


def read_file() -> list[list[int]]:
    return [[int(char) for char in trail.strip("\n")] for trail in open(FILENAME[0], 'r')]


def check_move_left(coord: tuple[int, int], grid: list[list[int]]) -> bool:
    if coord[0] > 0:
        value_at_coordinate = get_value_for_coordinate(coord, grid)
        next_coordinate = get_next_coordinate(coord, "left")
        value_at_next_coordinate = get_value_for_coordinate(next_coordinate, grid)
        if int(value_at_coordinate)+1 == int(value_at_next_coordinate):
            return True
    return False


def check_move_right(coord: tuple[int, int], grid: list[list[int]]) -> bool:
    if coord[0] < len(grid[0]) - 1:
        value_at_coordinate = get_value_for_coordinate(coord, grid)
        next_coordinate = get_next_coordinate(coord, "right")
        value_at_next_coordinate = get_value_for_coordinate(next_coordinate, grid)
        if int(value_at_coordinate)+1 == int(value_at_next_coordinate):
            return True
    return False


def check_move_top(coord: tuple[int, int], grid: list[list[int]]) -> bool:
    if coord[1] > 0:
        value_at_coordinate = get_value_for_coordinate(coord, grid)
        next_coordinate = get_next_coordinate(coord, "top")
        value_at_next_coordinate = get_value_for_coordinate(next_coordinate, grid)
        if int(value_at_coordinate)+1 == int(value_at_next_coordinate):
            return True
    return False


def check_move_bottom(coord: tuple[int, int], grid: list[list[int]]) -> bool:
    if coord[1] < len(grid) - 1:
        value_at_coordinate = get_value_for_coordinate(coord, grid)
        next_coordinate = get_next_coordinate(coord, "bottom")
        value_at_next_coordinate = get_value_for_coordinate(next_coordinate, grid)
        if int(value_at_coordinate)+1 == int(value_at_next_coordinate):
            return True
    return False


def get_value_for_coordinate(coordinate: tuple[int, int], grid: list[list[int]]) -> int:
    return int(grid[coordinate[1]][coordinate[0]])


def get_next_coordinate(coordinate: tuple[int, int], direction: str) -> tuple[int, int]:
    return (coordinate[0]+directions[direction][0], coordinate[1]+directions[direction][1])


def part1() -> int:
    grid = read_file()
    starting_points = defaultdict(set)
    for y, line in enumerate(grid):
        for x, height in enumerate(line):
            if height == 0:
                starting_points[int(height)].add((x, y))

    ret = 0
    for starting_point in starting_points[0]:
        points_to_check = defaultdict(set)
        points_to_check[0] = {starting_point}

        for i in range(9):
            for point in points_to_check[i]:
                if check_move_bottom(point, grid):
                    next_coordinate = get_next_coordinate(point, "bottom")
                    value_at_next_coordinate = get_value_for_coordinate(next_coordinate, grid)
                    points_to_check[int(value_at_next_coordinate)].add(next_coordinate)

                if check_move_top(point, grid):
                    next_coordinate = get_next_coordinate(point, "top")
                    value_at_next_coordinate = get_value_for_coordinate(next_coordinate, grid)
                    points_to_check[int(value_at_next_coordinate)].add(next_coordinate)

                if check_move_left(point, grid):
                    next_coordinate = get_next_coordinate(point, "left")
                    value_at_next_coordinate = get_value_for_coordinate(next_coordinate, grid)
                    points_to_check[int(value_at_next_coordinate)].add(next_coordinate)

                if check_move_right(point, grid):
                    next_coordinate = get_next_coordinate(point, "right")
                    value_at_next_coordinate = get_value_for_coordinate(next_coordinate, grid)
                    points_to_check[int(value_at_next_coordinate)].add(next_coordinate)

                if value_at_next_coordinate == 9:
                    points_to_check[int(value_at_next_coordinate)].add(next_coordinate)

        ret += len(points_to_check[9])
    return ret


def part2() -> int:
    grid = read_file()
    starting_positions = []
    end_positions = []
    unique_paths = set()

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                starting_positions.append((x, y))
            elif grid[y][x] == 9:
                end_positions.append((x, y))

    for start in starting_positions:
        backtrack(grid, start[0], start[1], [start], end_positions, unique_paths)
    return len(unique_paths)


def backtrack(grid: list[list[int]], x: int, y: int, path: list[tuple[int, int]], end_positions: list[tuple[int, int]], unique_paths: set[tuple[tuple[int, int]]]) -> None:
    if (x, y) in end_positions:
        unique_paths.add(tuple(path))
        return

    for dx, dy in directions.values():
        new_x = x + dx
        new_y = y + dy

        if (0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and (new_x, new_y) not in path and grid[y][x]+1 == grid[new_y][new_x]):
            path.append((new_x, new_y))
            backtrack(grid, new_x, new_y, path, end_positions, unique_paths)
            path.pop()


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
