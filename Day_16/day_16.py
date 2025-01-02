import heapq
from collections import defaultdict

FILENAME = ["input.txt", "testInput.txt", "testInput2.txt"]

directions = {
    "top": (-1, 0),
    "bottom": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


def read_file() -> list[int]:
    return [[subline for subline in line.strip("\n")] for line in open(FILENAME[0], 'r')]


def get_neighbours(grid: list[list[str]], point: tuple[int, int], direction: str) -> list[tuple[int, int, int, str]]:
    row, col = point
    neighbours = []

    for new_direction, (dr, dc) in directions.items():
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] != "#":
            cost = 1 if direction == new_direction else 1001
            neighbours.append((cost, new_row, new_col, new_direction))

    return neighbours


def dijkstra(grid: list[list[str]], startpoint: tuple[int, int], endpoint: tuple[int, int]) -> int:
    priority_queue = [(0, startpoint[0], startpoint[1], 'right')]
    heapq.heapify(priority_queue)

    distance = defaultdict(lambda: float('inf'))
    distance[(startpoint[0], startpoint[1], 'right')] = 0
    previous = defaultdict(list)

    while priority_queue:
        cost, row, col, direction = heapq.heappop(priority_queue)

        if (row, col) == endpoint:
            return cost

        for move_cost, new_row, new_col, new_direction in get_neighbours(grid, (row, col), direction):
            new_cost = cost + move_cost

            if new_cost < distance[(new_row, new_col, new_direction)]:
                distance[(new_row, new_col, new_direction)] = new_cost
                heapq.heappush(priority_queue, (new_cost, new_row, new_col, new_direction))
                previous[(new_row, new_col, new_direction)] = (row, col, direction)


def get_start_and_end(grid: list[list[str]]) -> tuple[tuple[int, int]]:
    for row, _ in enumerate(grid):
        if grid[row].count("E") > 0:
            endpoint = (row, grid[row].index("E"))
        elif grid[row].count("S") > 0:
            startpoint = (row, grid[row].index("S"))
    return startpoint, endpoint


def part1() -> int:
    grid = read_file()
    startpoint, endpoint = get_start_and_end(grid)
    return dijkstra(grid, startpoint, endpoint)


def part2() -> int:
    return 0


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
