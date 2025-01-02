FILENAME = ["input.txt", "testInput.txt", "testInput2.txt"]


def read_file() -> tuple[list[str], list[str]]:
    file_1 = []
    file_2 = []
    with open(FILENAME[1], 'r') as file:
        for line in file:
            numbers = [item for item in str(
                line.strip("\n")).split(" ") if item]
            file_1.append(int(numbers[0]))
            file_2.append(int(numbers[-1]))
    return file_1, file_2


def part1() -> int:
    file_1, file_2 = read_file()
    file_1 = sorted([item for item in file_1])
    file_2 = sorted([item for item in file_2])

    return sum([abs(file_2[i] - file_1[i]) for i in range(len(file_1))])


def part2() -> int:
    file_1, file_2 = read_file()
    return sum([file_1[i] * file_2.count(file_1[i])
                for i in range(len(file_1))])


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
