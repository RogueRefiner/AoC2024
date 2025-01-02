import itertools

FILENAME = ["input.txt", "testInput.txt"]


def read_file() -> list[int]:
    # return [[int(line.split(": ")[0]), [int(x) for x in line.split(": ")[1].split(" ")]] for line in open(FILENAME[1], 'r')]
    input_list = []
    with open(FILENAME[0], 'r') as file:
        for line in file:
            line = line.split(": ")
            line[1] = [int(x) for x in line[1].split(" ")]
            line[0] = int(line[0])
            input_list.append(line)
    return input_list


def generate_all_operations(num_numbers: int, part_1: bool) -> list[tuple[str]]:
    if part_1:
        operations = ["+", "*"]
    else:
        operations = ["+", "*", "||"]

    operation_lists = [operations]*(num_numbers-1)
    return list(itertools.product(*operation_lists))


def solve_equations(result, numbers, operations):
    for operation in operations:
        res = 0
        for i in range(len(numbers)):
            if i == 0:
                res += int(f'{int(numbers[i])}')
            else:
                if operation[i-1] == "+":
                    res += int(f'{int(numbers[i])}')
                elif operation[i-1] == "*":
                    res *= int(f'{int(numbers[i])}')
                elif operation[i-1] == "||":
                    res = int("".join(str(res)+str(numbers[i])))
            if res > result:
                break
        if res == result:
            return res
    return 0


def part1() -> int:
    input_list = read_file()
    ret = 0

    for line in input_list:
        result = line[0]
        numbers = line[1]
        operations = generate_all_operations(len(numbers), True)
        ret += solve_equations(result, numbers, operations)
    return ret


def part2() -> int:
    input_list = read_file()
    ret = 0

    for line in input_list:
        result = line[0]
        numbers = line[1]
        operations = generate_all_operations(len(numbers), False)
        ret += solve_equations(result, numbers, operations)
    return ret


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
