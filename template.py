FILENAME = ["input.txt", "testInput.txt"]


def read_file() -> list[int]:
    input_list = []
    with open(FILENAME[1], 'r') as file:
        for line in file:
            pass
    return input_list


def part1() -> int:
    pass


def part2() -> int:
    pass


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
