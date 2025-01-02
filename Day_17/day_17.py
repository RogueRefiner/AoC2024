FILENAME = ["input.txt", "testInput.txt"]


def read_file() -> list[int]:
    program = []
    registers = {}
    with open(FILENAME[0], 'r') as file:
        for line in file:
            if "Register" in line:
                line = line.strip("\n").split(": ")
                registers[line[0][-1]] = int(line[1])
            elif "Program" in line:
                line = line.strip("\n").split(": ")
                program = [int(i) for i in line[1] if i.isdigit()]

    return program, registers


def calculate_combo_operand(value: int, registers: dict[int]) -> int:
    match(value % 8):
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return registers['A'] % 8
        case 5:
            return registers['B'] % 8
        case 6:
            return registers['C'] % 8
        case 7:
            raise Exception(f"Invalid value: {value}")


def execute_op_code(op_code: tuple[int, int], registers: dict[int], ptr: int, output: str) -> str:
    match(op_code[0]):
        case 0:
            registers['A'] = int(registers['A'] / (2**calculate_combo_operand(op_code[1], registers)))
        case 1:
            registers['B'] = registers['B'] ^ op_code[1]
        case 2:
            registers['B'] = calculate_combo_operand(op_code[1], registers)
        case 3:
            if registers['A'] != 0:
                return op_code[1], output
        case 4:
            registers['B'] = registers['B'] ^ registers['C']
        case 5:
            output += str(calculate_combo_operand(op_code[1], registers))
        case 6:
            registers['B'] = int(registers['A'] / (2**calculate_combo_operand(op_code[1], registers)))
        case 7:
            registers['C'] = int(registers['A'] / (2**calculate_combo_operand(op_code[1], registers)))
    return ptr+2, output


def part1() -> int:
    ptr = 0
    program, registers = read_file()
    output = []
    while ptr < len(program):
        op_code = (program[ptr], program[ptr+1])
        ptr, output = execute_op_code(op_code, registers, ptr, output)

    return ",".join(output)


def part2() -> int:
    pass


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
