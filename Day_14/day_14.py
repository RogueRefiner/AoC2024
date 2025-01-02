FILENAME = ["input.txt", "testInput.txt"]


def read_file() -> tuple[list[tuple[int, int], list[tuple[int, int]]]]:
    positions = []
    velocities = []

    with open(FILENAME[0], 'r') as file:
        for _, line in enumerate(file):
            line = line.split(" ")
            position_list = line[0].split("=")[1].split(",")
            velocity_list = line[1].split("=")[1].split(",")
            positions.append((int(position_list[0]), int(position_list[1])))
            velocities.append((int(velocity_list[0]), int(velocity_list[1])))
    return positions, velocities


def part1() -> int:
    positions, velocities = read_file()
    columns = 101
    rows = 103
    seconds = 100
    q1, q2, q3, q4 = ([] for _ in range(4))
    safety_factor = 1

    for j in range(len(positions)):
        for _ in range(seconds):
            new_c = (positions[j][0] + velocities[j][0])
            new_r = (positions[j][1] + velocities[j][1])

            if new_c < 0:
                new_c = columns + new_c
            elif new_c > columns - 1:
                new_c = new_c - columns

            if new_r < 0:
                new_r = rows + new_r
            elif new_r > rows - 1:
                new_r = new_r - rows

            positions[j] = (new_c, new_r)

        if positions[j][1] < ((rows - 1) // 2) and positions[j][0] > ((columns - 1) // 2):
            q1.append(positions[j])
        elif positions[j][1] < ((rows - 1) // 2) and positions[j][0] < ((columns - 1) // 2):
            q2.append(positions[j])
        elif positions[j][1] > ((rows - 1) // 2) and positions[j][0] < ((columns - 1) // 2):
            q3.append(positions[j])
        elif positions[j][1] > ((rows - 1) // 2) and positions[j][0] > ((columns - 1) // 2):
            q4.append(positions[j])
    return safety_factor * len(q1) * len(q2) * len(q3) * len(q4)


def part2() -> int:
    positions, velocities = read_file()
    columns = 101
    rows = 103
    number_of_robots = len(positions)
    grid = [["." for _ in range(columns)] for _ in range(rows)]

    for i in range(1, 8000):
        for j in range(len(positions)):
            new_c = (positions[j][0] + velocities[j][0])
            new_r = (positions[j][1] + velocities[j][1])

            if new_c < 0:
                new_c = columns + new_c
            elif new_c > columns - 1:
                new_c = new_c - columns

            if new_r < 0:
                new_r = rows + new_r
            elif new_r > rows - 1:
                new_r = new_r - rows

            positions[j] = (new_c, new_r)

        tree = open("tree.txt", "w")
        if len(set(positions)) == number_of_robots:
            for position in positions:
                c, r = position
                if grid[r][c] == ".":
                    grid[r][c] = "1"
            for row in grid:
                tree.write(f'{"".join(row)}\n')
            return i


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
