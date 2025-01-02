FILENAME = ["input.txt", "testInput.txt"]


def read_file() -> tuple[list[str], list[str]]:
    desired_designs = []
    towels = []
    with open(FILENAME[0], 'r') as file:
        for idx, line in enumerate(file):
            line = line.strip("\n")
            if idx == 0:
                for towel in line.split(", "):
                    towels.append(towel)
            elif line != "":
                desired_designs.append(line)
    return towels, desired_designs


def find_all_valid(design: str, towels: list[str], memo: dict = None) -> int:
    if memo is None:
        memo = {}

    if design in memo:
        return memo[design]

    if not design:
        return 1

    count = 0

    for towel in towels:
        if design.startswith(towel):
            count += find_all_valid(design[len(towel):], towels, memo)

    memo[design] = count
    return count


def find_valid(design: str, towels: list[str], memo: dict = None) -> bool:
    if memo is None:
        memo = {}

    if design in memo:
        return memo[design]

    if not design:
        return True

    for towel in towels:
        if design.startswith(towel):
            if find_valid(design[len(towel):], towels, memo):
                memo[design] = True
                return True

    memo[design] = False
    return False


def part1() -> int:
    towels, desired_designs = read_file()

    possible_designs = 0
    for design in desired_designs:
        possible_designs += find_valid(design, towels)

    return possible_designs


def part2() -> int:
    towels, desired_designs = read_file()

    possible_designs = 0
    for design in desired_designs:
        possible_designs += find_all_valid(design, towels)

    return possible_designs


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
