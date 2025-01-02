FILENAME = ["input.txt", "testInput.txt", "testInput2.txt"]


def read_file() -> tuple[list[list[str]], str]:
    grid = []
    commands = ""
    with open(FILENAME[1], 'r') as file:
        for line in file:
            line = line.strip("\n")
            if line.count("#") >= 1:
                grid.append([char for char in line])
            elif line != "":
                commands += line

    return grid, commands


def print_grid(grid: list[list[str]]) -> None:
    for row in grid:
        print("".join(row))
    return


def execute_command(grid: list[list[str]], command: str, robot: tuple[int, int]) -> tuple[list[list[str]], tuple[int, int]]:
    r, c = robot
    match command:
        case "<":
            if c-1 > 0 and grid[r][c-1] == "#":
                return grid, robot

            elif c-1 > 0 and grid[r][c-1] == "O":
                scan_c = c-1
                while scan_c > 0:
                    if grid[r][scan_c-1] == "#":
                        return grid, robot
                    elif grid[r][scan_c-1] == ".":
                        grid[r][scan_c-1], grid[r][c-1] = grid[r][c-1], grid[r][scan_c-1]
                        grid[r][c], grid[r][c-1] = grid[r][c-1], grid[r][c]
                        robot = (r, c-1)
                        return grid, robot
                    scan_c -= 1
                return grid, robot

            elif c-1 > 0 and grid[r][c-1] == ".":
                grid[r][c], grid[r][c-1] = grid[r][c-1], grid[r][c]
                robot = (r, c-1)
            return grid, robot

        case ">":
            column_len = len(grid[0]) - 1
            if c+1 < column_len and grid[r][c+1] == "#":
                return grid, robot

            elif c+1 < column_len and grid[r][c+1] == "O":
                scan_c = c + 1
                while scan_c < column_len:
                    if grid[r][scan_c+1] == "#":
                        return grid, robot
                    elif grid[r][scan_c+1] == ".":
                        grid[r][scan_c+1], grid[r][c+1] = grid[r][c+1], grid[r][scan_c+1]
                        grid[r][c], grid[r][c+1] = grid[r][c+1], grid[r][c]
                        robot = (r, c+1)
                        return grid, robot
                    scan_c += 1

            elif c+1 < column_len and grid[r][c+1] == ".":
                grid[r][c], grid[r][c+1] = grid[r][c+1], grid[r][c]
                robot = (r, c+1)
                return grid, robot
            return grid, robot

        case "v":
            row_len = len(grid) - 1
            if r+1 < row_len and grid[r+1][c] == "#":
                return grid, robot

            elif r+1 < row_len and grid[r+1][c] == "O":
                scan_r = r + 1
                while scan_r < row_len:
                    if grid[scan_r+1][c] == "#":
                        return grid, robot
                    elif grid[scan_r+1][c] == ".":
                        grid[scan_r+1][c], grid[r+1][c] = grid[r+1][c], grid[scan_r+1][c]
                        grid[r][c], grid[r+1][c] = grid[r+1][c], grid[r][c]
                        robot = (r+1, c)
                        return grid, robot
                    scan_r += 1

            elif r+1 < row_len and grid[r+1][c] == ".":
                grid[r][c], grid[r+1][c] = grid[r+1][c], grid[r][c]
                robot = (r+1, c)
                return grid, robot
            return grid, robot

        case "^":
            if r-1 > 0 and grid[r-1][c] == '#':
                return grid, robot

            elif r-1 > 0 and grid[r-1][c] == "O":
                scan_r = r - 1
                while scan_r > 0:
                    if grid[scan_r-1][c] == "#":
                        return grid, robot
                    elif grid[scan_r-1][c] == ".":
                        grid[scan_r-1][c], grid[r-1][c] = grid[r-1][c], grid[scan_r-1][c]
                        grid[r][c], grid[r-1][c] = grid[r-1][c], grid[r][c]
                        robot = (r-1, c)
                        return grid, robot
                    scan_r -= 1

            elif r - 1 > 0 and grid[r-1][c] == ".":
                grid[r][c], grid[r-1][c] = grid[r-1][c], grid[r][c]
                robot = (r-1, c)
                return grid, robot
            return grid, robot


def part1() -> int:
    grid, commands = read_file()

    for row in range(len(grid)):
        if grid[row].count("@") > 0:
            robot = (row, grid[row].index("@"))

    for command in commands:
        grid, robot = execute_command(grid, command, robot)

    gps_score = 0
    for row in range(len(grid)):
        if grid[row].count("O") > 0:
            for column in range(len(grid[0])):
                if grid[row][column] == "O":
                    gps_score += 100*row + column

    return gps_score


def transform_grid(grid: list[list[str]]) -> list[list[str]]:
    for row in range(len(grid)):
        new_row = []
        for column in range(len(grid[-1])):
            if grid[row][column] == "#":
                new_row += ["#", "#"]
            elif grid[row][column] == "O":
                new_row += ["[", "]"]
            elif grid[row][column] == ".":
                new_row += [".", "."]
            elif grid[row][column] == "@":
                new_row += ["@", "."]
        grid[row] = new_row
    return grid


def part2() -> int:
    pass


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
