from collections import defaultdict

FILENAME = ["input.txt", "testInput.txt"]


def read_file() -> list[str]:
    return open(FILENAME[0], 'r').read().split(" ")


def part1() -> int:
    stone_arrangement = read_file()
    for _ in range(25):
        new_arrangement = []
        for number in stone_arrangement:
            if int(number) == 0:
                new_arrangement.append("1")
            elif len(number) % 2 == 0:
                middle = len(number) // 2
                new_arrangement.append(str(int(number[:middle])))
                new_arrangement.append(str(int(number[middle:])))
            else:
                new_arrangement.append(str(int(number)*2024))
        stone_arrangement = new_arrangement

    return len(stone_arrangement)


def blink(stone_dict: dict[str, int]) -> dict[str, int]:
    new_stone_dict = defaultdict(int)
    for stone, count in stone_dict.items():
        if int(stone) == 0:
            new_stone_dict["1"] += count
        elif len(stone) % 2 == 0:
            middle = len(stone) // 2
            new_stone_dict[str(int(stone[:middle]))] += count
            new_stone_dict[str(int(stone[middle:]))] += count
        else:
            new_stone_dict[str(int(stone)*2024)] += count
    return new_stone_dict


def part2() -> int:
    stone_dict = defaultdict(int)
    stone_arrangement = read_file()
    for number in stone_arrangement:
        stone_dict[number] += 1

    for _ in range(75):
        stone_dict = blink(stone_dict)

    return sum(stone_dict.values())


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
