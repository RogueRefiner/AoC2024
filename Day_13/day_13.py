FILENAME = ["input.txt", "testInput.txt"]


def read_file() -> list[int]:
    equations = []
    with open(FILENAME[0], 'r') as file:
        equation = []
        for line in file:
            if line.strip("\n") == "":
                equations.append(equation)
                equation = []
            else:
                equation.append(line.strip("\n").split(": "))
    equations.append(equation)
    return equations


def build_equation_systems(input_list: list[list[str]], add: int) -> list[list[int]]:
    equation_systems = []
    for equation in input_list:
        first_equation = []
        second_equation = []
        for i in range(len(equation)):
            if i < len(equation) - 1:
                first_equation.append(int(equation[i][1].split("+")[1].split(", ")[0]))
                second_equation.append(int(equation[i][1].split("+")[2]))
            else:
                first_equation.append(int(equation[i][1].split("=")[1].split(", ")[0])+add)
                second_equation.append(int(equation[i][1].split("=")[2])+add)
        equation_systems.append([first_equation, second_equation])
    return equation_systems


def solve_equations(equation_systems: list[list[int]], part: str) -> int:
    tokens = 0
    for equation_system in equation_systems:
        d = (equation_system[0][0]*equation_system[1][1]-equation_system[1][0]*equation_system[0][1])
        d1 = (equation_system[0][2]*equation_system[1][1] - equation_system[1][2]*equation_system[0][1])
        d2 = (equation_system[0][0]*equation_system[1][2] - equation_system[1][0]*equation_system[0][2])

        x = int(d1 / d)
        y = int(d2 / d)

        first_equation_solved = x*int(equation_system[0][0]) + y * \
            int(equation_system[0][1]) == int(equation_system[0][2])
        second_equation_solved = x*int(equation_system[1][0]) + y * \
            int(equation_system[1][1]) == int(equation_system[1][2])

        if (0 < x <= 100 and 0 < y <= 100 and first_equation_solved and second_equation_solved and part == "Part1"):
            tokens += 3*x+y
        elif (first_equation_solved and second_equation_solved and part == "Part2"):
            tokens += 3*x+y

    return tokens


def part1() -> int:
    input_list = read_file()

    add = 0
    equation_systems = build_equation_systems(input_list, add)
    tokens = solve_equations(equation_systems, "Part1")

    return int(tokens)


def part2() -> int:
    input_list = read_file()

    add = 10000000000000
    equation_systems = build_equation_systems(input_list, add)
    tokens = solve_equations(equation_systems, "Part2")

    return int(tokens)


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
