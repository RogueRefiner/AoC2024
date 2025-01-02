FILENAME = ["input.txt", "testInput.txt"]


def read_file() -> list[int]:
    input_list = []
    with open(FILENAME[0], 'r') as file:
        for line in file:
            input_list.append([int(item) for item in
                               line.strip("\n").split(" ") if item])
    return input_list


def is_safe(sublist: list[int]) -> bool:
    increasing = sublist[1] > sublist[0]
    for i in range(len(sublist) - 1):
        diff = abs(sublist[i+1] - sublist[i])
        if diff < 1 or diff > 3 or (increasing and sublist[i] > sublist[i+1]) or (not increasing and sublist[i] < sublist[i+1]):
            return False
    return True


def can_tolerate_one_bad_level(sublist: list[int]) -> bool:
    for i in range(len(sublist)):
        modified = sublist[:i] + sublist[i+1:]
        if is_safe(modified):
            return True
    return False


def part1() -> int:
    input_list = read_file()
    safe = 0
    for sublist in input_list:
        safe += is_safe(sublist)
    return safe


def part2() -> int:
    input_list = read_file()
    safe = 0
    for sublist in input_list:
        safe += is_safe(sublist) or can_tolerate_one_bad_level(sublist)
    return safe


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
