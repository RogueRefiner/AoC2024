import heapq
from collections import defaultdict

FILENAME = ["input.txt", "testInput.txt"]

directions = {
    "top": (-1, 0),
    "bottom": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


def read_file() -> list[int]:
    return [(int(line.strip("\n").split(",")[0]), int(line.strip("\n").split(",")[1])) for line in open(FILENAME[0])]


def print_grid(grid: list[list[str]]) -> None:
    for row in grid:
        print(row)


def bfs(grid: list[list[str]], start_position: tuple[int, int], end_position: tuple[int, int], part: str) -> int:
    queue = [start_position]
    visited = set()
    visited.add(start_position)
    parent = {}

    while queue:
        r, c = queue.pop(0)

        if (r, c) == end_position and part == "Part1":
            return reconstruct_path(parent, start_position, end_position)
        elif (r, c) == end_position and part == "Part2":
            return 1

        for dr, dc in directions.values():
            new_r, new_c = r+dr, c+dc

            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] != "#" and (new_r, new_c) not in visited:
                queue.append((new_r, new_c))
                parent[(new_r, new_c)] = (r, c)
                visited.add((new_r, new_c))
    return 0


def reconstruct_path(parent: dict[tuple[int, int]], start_position: tuple[int, int], end_position: tuple[int, int]) -> int:
    path = []
    current = end_position
    while current != start_position:
        path.append(current)
        current = parent[current]
    return len(path)


def part1() -> int:
    corrupted = read_file()[:1024]
    row = 71
    column = 71
    start_position = (0, 0)
    end_position = (row-1, column-1)

    grid = [["." for _ in range(column)] for _ in range(row)]

    for byte in corrupted:
        grid[byte[1]][byte[0]] = '#'

    print(bfs(grid, start_position, end_position, "Part1"))


def part2() -> int:
    corrupted = read_file()
    row = 71
    column = 71
    start_position = (0, 0)
    end_position = (row-1, column-1)

    grid = [["." for _ in range(column)] for _ in range(row)]
    for i in range(len(corrupted)):
        grid[corrupted[i][1]][corrupted[i][0]] = '#'

        if bfs(grid, start_position, end_position, "Part2") == 0:
            break

    return f'{corrupted[i][0]},{corrupted[i][1]}'


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
