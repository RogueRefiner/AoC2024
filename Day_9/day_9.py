FILENAME = ["input.txt", "testInput.txt"]


def read_file() -> str:
    return "".join([char for char in open(FILENAME[0], 'r')])


def calculate_checksum(disk: list[str]) -> int:
    ret = 0
    for idx, num in enumerate(disk):
        if disk[idx] == ".":
            continue

        ret += idx*(int(num))
    return ret


def transform_disk_map_representation(disk_map: list[str]) -> list[str]:
    sorted_input = []
    id_number = 0
    for idx, num in enumerate(disk_map):
        if idx % 2 == 1:
            id_number += 1
            sorted_input.extend(["."] * int(num))
        else:
            sorted_input.extend([str(id_number)] * int(num))
    return sorted_input


def rearrange_files(disk: list[str]) -> list[str]:
    while "." in disk:
        idx = disk.index(".")
        disk[idx], disk[-1] = disk[-1], disk[idx]
        disk.pop()
    return disk


def build_disk(tuple_represenation: list[list[str | int]]) -> list[str]:
    disk = []
    for tple in tuple_represenation:
        occurrences_of_file = tple[1]
        file_id = tple[0]
        for _ in range(occurrences_of_file):
            disk.append(str(file_id))
    return disk


def build_tuple_represenations(disk_map: str) -> tuple[list[list[int | str]], list[list[int | str]]]:
    files_and_free_spaces = []
    files = []
    for idx, num in enumerate(disk_map):
        if idx % 2 == 1 and int(num) > 0:
            files_and_free_spaces.append([".", int(num)])
        elif idx % 2 == 0:
            files_and_free_spaces.append([idx//2, int(num)])
            files.append((idx//2, int(num)))
    return files_and_free_spaces, files


def combine_adjacent_free_spaces(files_and_free_spaces: list[list[int | str]]) -> list[list[int | str]]:
    for j in range(len(files_and_free_spaces)):
        if j < len(files_and_free_spaces) - 1 and files_and_free_spaces[j][0] == "." and files_and_free_spaces[j+1][0] == ".":
            files_and_free_spaces[j] = [
                ".", files_and_free_spaces[j][1]+files_and_free_spaces[j+1][1]]
            del files_and_free_spaces[j+1]
    return files_and_free_spaces


def move_files_into_free_spaces(files: list[list[int | str]], files_and_free_spaces: list[list[int | str]]) -> list[list[int | str]]:
    for tple in reversed(files):
        terminate = False
        for i in range(len(files_and_free_spaces)):
            # only swap to indices in front of the tuple
            if files_and_free_spaces[i] == [tple[0], tple[1]]:
                terminate = True
                break
            if files_and_free_spaces[i][0] == "." and files_and_free_spaces[i][1] >= tple[1]:
                if int(files_and_free_spaces[i][1]) - tple[1] == 0:
                    del files_and_free_spaces[i]  # del [".", 0]
                else:
                    files_and_free_spaces[i][1] = int(files_and_free_spaces[i][1]) - tple[1]
                to_del = files_and_free_spaces.index([tple[0], tple[1]])
                # free disk space previously occupied by file
                files_and_free_spaces[to_del] = [".", tple[1]]
                # insert moved file at the new position
                files_and_free_spaces.insert(i, [tple[0], tple[1]])
                terminate = True
            if terminate:
                files_and_free_spaces = combine_adjacent_free_spaces(files_and_free_spaces)
                break
    return files_and_free_spaces


def part1() -> int:
    disk_map = read_file()
    disk = transform_disk_map_representation(disk_map)
    disk = rearrange_files(disk)
    return calculate_checksum(disk)


def part2() -> int:
    disk_map = read_file()
    files_and_free_spaces, files = build_tuple_represenations(disk_map)
    files_and_free_spaces = move_files_into_free_spaces(files, files_and_free_spaces)
    disk = build_disk(files_and_free_spaces)
    return calculate_checksum(disk)


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
