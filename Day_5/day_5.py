from collections import defaultdict

FILENAME = ["input.txt", "testInput.txt"]


def read_file() -> tuple[list[int, int], list[int]]:
    input_list = []
    rules = defaultdict(list)
    with open(FILENAME[0], 'r') as file:
        for line in file:
            line = line.strip("\n")
            if "|" in line:
                tple = line.split("|")
                rules[int(tple[0])].append(int(tple[1]))
            elif line != "":
                input_list.append([int(i) for i in line.split(",")])
    return rules, input_list


def check_update(rules: dict[int], update: list[int]) -> int:
    terminate = False
    for idx, page in enumerate(update):
        for i in range(idx+1, len(update)):
            if update[i] not in rules[page]:
                update[i], update[idx] = update[idx], update[i]
                terminate = True
                break
        if terminate:
            return 0
    if terminate == False:
        return update[len(update) // 2]
    return 0


def check_if_update_broken(update: list[int], rules: dict[list]) -> bool:
    for idx, page in enumerate(update):
        for i in range(idx+1, len(update)):
            if update[i] not in rules[page]:
                return True
    return False


def part1() -> int:
    rules, input_list = read_file()
    ret = 0
    for update in input_list:
        ret += check_update(rules, update)
    return ret


def reorder_broken_updates(broken_update: list[int], rules: dict[list]) -> int:
    update_correct = False
    while update_correct == False:
        middle_value = check_update(rules, broken_update)
        if middle_value in rules.keys():
            return middle_value


def part2() -> int:
    rules, input_list = read_file()
    ret = 0
    broken_updates = []
    for update in input_list:
        if check_if_update_broken(update, rules):
            broken_updates.append(update)

    for update in broken_updates:
        ret += reorder_broken_updates(update, rules)
    return ret


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
"""         
        update_correct = False
        while update_correct == False:
            middle_value = check_update(rules, update)
            if middle_value in rules.keys():
                ret += middle_value
                update_correct = True
 """
