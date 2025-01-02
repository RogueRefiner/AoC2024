import re

FILENAME = ["input.txt", "testInput.txt"]


def read_file(part1: bool) -> list[list[str]]:
    input_list = []

    if part1:
        pattern = r'mul\(\d+,\d+\)'
    else:
        pattern = r"don't\(\)?|do\(\)?|mul\(\d+,\d+\)"

    with open(FILENAME[0], 'r') as file:
        for line in file:
            input_list.append(re.findall(pattern, line))
    return input_list


def extract_numbers_from_string(strng: str) -> list[int]:
    return strng.replace("mul(", "").replace(")", "").replace(
        ")", "").replace(",", " ").split(" ")


def part1() -> int:
    input_list = read_file(True)
    ret = 0
    for line in input_list:
        for strng in line:
            numbers = extract_numbers_from_string(strng)
            ret += int(numbers[0]) * int(numbers[1])
    return ret


def part2() -> int:
    input_list = read_file(False)
    ret = 0
    active = True
    enabled_statements = []

    for line in input_list:
        for strng in line:
            if strng == "don't()":
                active = False
            if strng == "do()":
                active = True
            if active and strng != "do()":
                enabled_statements.append(strng)

    for strng in enabled_statements:
        numbers = extract_numbers_from_string(strng)
        ret += int(numbers[0]) * int(numbers[1])
    return ret


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
