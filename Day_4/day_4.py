FILENAME = ["input.txt", "testInput.txt"]


def read_file() -> list[list[str]]:
    input_list = []
    with open(FILENAME[0], 'r') as file:
        for line in file:
            input_list.append(line.strip("\n"))
    return input_list


def part1() -> int:
    input_list = read_file()
    count = 0
    for i, line in enumerate(input_list):
        for j, char in enumerate(line):
            if char == "X" and j <= len(line) - 4:
                if input_list[i][j+1] == "M" and input_list[i][j+2] == "A" and input_list[i][j+3] == "S":
                    count += 1
            if char == "X" and i <= len(input_list) - 4:
                if input_list[i+1][j] == "M" and input_list[i+2][j] == "A" and input_list[i+3][j] == "S":
                    count += 1
            if char == "X" and i >= 3 and j <= len(line) - 4:
                if input_list[i-1][j+1] == "M" and input_list[i-2][j+2] == "A" and input_list[i-3][j+3] == "S":
                    count += 1
            if char == "X" and i <= len(input_list) - 4 and j <= len(line) - 4:
                if input_list[i+1][j+1] == "M" and input_list[i+2][j+2] == "A" and input_list[i+3][j+3] == "S":
                    count += 1

            if char == "S" and i <= len(input_list) - 4:
                if input_list[i+1][j] == "A" and input_list[i+2][j] == "M" and input_list[i+3][j] == "X":
                    count += 1
            if char == "S" and i >= 3 and j <= len(line) - 4:
                if input_list[i-1][j+1] == "A" and input_list[i-2][j+2] == "M" and input_list[i-3][j+3] == "X":
                    count += 1
            if char == "S" and i <= len(input_list) - 4 and j <= len(line) - 4:
                if input_list[i+1][j+1] == "A" and input_list[i+2][j+2] == "M" and input_list[i+3][j+3] == "X":
                    count += 1
            if char == "S" and j <= len(line) - 4:
                if input_list[i][j+1] == "A" and input_list[i][j+2] == "M" and input_list[i][j+3] == "X":
                    count += 1

    return count


def part2() -> int:
    input_list = read_file()
    count = 0

    for i, line in enumerate(input_list):
        for j, char in enumerate(line):
            if char == "M" and j <= len(line) - 3 and i <= len(input_list) - 3:
                if input_list[i][j+2] == "S" and input_list[i+1][j+1] == "A" and input_list[i+2][j] == "M" and input_list[i+2][j+2] == "S":
                    count += 1
                elif input_list[i][j+2] == "M" and input_list[i+1][j+1] == "A" and input_list[i+2][j] == "S" and input_list[i+2][j+2] == "S":
                    count += 1
            if char == "S" and j <= len(line) - 3 and i <= len(input_list) - 3:
                if input_list[i][j+2] == "S" and input_list[i+1][j+1] == "A" and input_list[i+2][j] == "M" and input_list[i+2][j+2] == "M":
                    count += 1
                elif input_list[i][j+2] == "M" and input_list[i+1][j+1] == "A" and input_list[i+2][j] == "S" and input_list[i+2][j+2] == "M":
                    count += 1

    return count


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
