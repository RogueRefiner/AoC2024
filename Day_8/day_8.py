from collections import defaultdict

FILENAME = ["input.txt", "testInput.txt", "testInput2.txt"]


def read_file() -> list[list[str]]:
    return [[char for char in line.strip("\n")] for line in open(FILENAME[0], 'r')]


def build_antennas_dict(input_list: list[list[str]]) -> dict[str, tuple[int, int]]:
    antennas = defaultdict(list)
    for y, line in enumerate(input_list):
        for x, antenna in enumerate(line):
            if antenna != ".":
                antennas[antenna].append((x, y))
    return antennas


def build_coordinate_changes_dict(antennas: dict[str, tuple[int, int]]) -> dict[tuple[int, int], list[tuple[int, int]]]:
    coordinate_changes_for_antinodes = defaultdict(list)
    for key in antennas.keys():
        for dict_idx, antenne in enumerate(antennas[key]):
            for antenna_idx in range(len(antennas[key])):
                if dict_idx != antenna_idx:
                    coordinate_change = (
                        antenne[0] - antennas[key][antenna_idx][0], antenne[1] - antennas[key][antenna_idx][1])
                    coordinate_changes_for_antinodes[antenne].append(
                        coordinate_change)
    return coordinate_changes_for_antinodes


def check_possible_antinode(possible_antinode: tuple[int, int], input_list: list[list[str]]) -> bool:
    return possible_antinode[0] < len(input_list[0]) and possible_antinode[0] >= 0 and possible_antinode[1] < len(input_list) and possible_antinode[1] >= 0


def part1() -> int:
    input_list = read_file()
    antennas = build_antennas_dict(input_list)
    coordinate_changes_for_antinodes = build_coordinate_changes_dict(antennas)

    antinodes = set()
    for node in coordinate_changes_for_antinodes.keys():
        for coordinate_changes in coordinate_changes_for_antinodes[node]:
            possible_antinode = (
                coordinate_changes[0] + node[0], coordinate_changes[1] + node[1])

            if check_possible_antinode(possible_antinode, input_list):
                antinodes.add(possible_antinode)

    return len(antinodes)


def part2() -> int:
    input_list = read_file()
    antennas = build_antennas_dict(input_list)
    coordinate_changes_for_antinodes = build_coordinate_changes_dict(antennas)

    antinodes = set()
    for node in coordinate_changes_for_antinodes.keys():
        antinodes.add(node)

        for coordinate_changes in coordinate_changes_for_antinodes[node]:
            possible_antinode = (coordinate_changes[0] + node[0],
                                 coordinate_changes[1] + node[1])

            while check_possible_antinode(possible_antinode, input_list):
                antinodes.add(possible_antinode)
                possible_antinode = (
                    possible_antinode[0] + coordinate_changes[0], possible_antinode[1] + coordinate_changes[1])

    return len(antinodes)


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
