from collections import defaultdict

FILENAME = ["input.txt", "testInput.txt", "testInput2.txt", "testInput3.txt", "testInput4.txt", "testInput5.txt"]

directions = {
    "top": (0, -1),
    "bottom": (0, 1),
    "left": (-1, 0),
    "right": (1, 0)
}


def read_file() -> list[list[str]]:
    return [line.strip("\n") for line in open(FILENAME[0])]


def find_all_unique_regions(garden_plots: list[list[str]]) -> dict[list[set[tuple[int, int]]]]:
    unique_regions = defaultdict(list)
    coordinates_of_each_plant_type = defaultdict(set)  # except size 1 regions

    for y, garden_row in enumerate(garden_plots):
        for x, plant_type in enumerate(garden_row):
            check_bottom = check_neighbour(x, y, 'bottom', plant_type, garden_plots)
            check_right = check_neighbour(x, y, 'right', plant_type, garden_plots)
            check_left = check_neighbour(x, y, 'left', plant_type, garden_plots)
            check_top = check_neighbour(x, y, 'top', plant_type, garden_plots)
            size_one_region = check_bottom and check_right and check_left and check_top
            if size_one_region:
                unique_regions[plant_type].append([(x, y)])
            else:
                coordinates_of_each_plant_type[plant_type].add((x, y))

    coordinates_of_each_plant_type = {
        key: sorted(values, key=lambda coord: (coord[0], coord[1])) for key, values in coordinates_of_each_plant_type.items()
    }

    for key in coordinates_of_each_plant_type:
        while len(coordinates_of_each_plant_type[key]) > 0:
            new_unique_regions = split_into_connected_regions(coordinates_of_each_plant_type[key])
            for unique_region in new_unique_regions:
                unique_regions[key].append(unique_region)

    return unique_regions


def split_into_connected_regions(coords: set[tuple[int, int]]):
    queue = [coords[0]]
    visited = {coords[0]}
    while queue:
        x, y = queue.pop()
        for dx, dy in directions.values():
            new_x = x + dx
            new_y = y + dy
            if (new_x, new_y) in coords and (new_x, new_y) not in visited:
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))

    for coordinate in visited:
        coords.remove(coordinate)

    return [visited]


def check_neighbour(x: int, y: int, direction: str, garden_plot: str, garden_plots: list[list[str]]) -> bool:
    return not (0 <= x+directions[direction][0] < len(garden_plots[0]) and 0 <= y+directions[direction][1] < len(garden_plots)
                and garden_plots[y+directions[direction][1]][x+directions[direction][0]] == garden_plot)


def calc_perimeter(region: list[tuple[int, int]]) -> int:
    perimeter = 0
    for x, y in region:
        for dx, dy in directions.values():
            if (x + dx, y + dy) not in region:
                perimeter += 1
    return perimeter


def calc_sides(region: list[tuple[int, int]]) -> int:
    count = 0
    scan_directions = ["backward", "forward"]
    for dx, dy in directions.values():
        checked = set()
        for plant in region:
            x, y = plant

            if (x, y) in checked:
                continue

            if (x+dx, y+dy) in region:
                continue

            count += 1

            for scan_direction in scan_directions:
                x, y = plant
                while (x, y) in region and (x+dx, y+dy) not in region:
                    checked.add((x, y))
                    # perpendicular scan -> scans orthogonal to movement
                    if scan_direction == "forward":
                        x += dy
                        y += dx
                    else:
                        x -= dy
                        y -= dx
    return count


def calc_fence_price(unique_regions: dict[list[set[tuple[int, int]]]], part: str) -> int:
    fence_price = 0
    for key in unique_regions:
        for region in unique_regions[key]:
            if part == "Part1":
                fence_price += len(region) * calc_perimeter(region)
            else:
                fence_price += len(region) * calc_sides(region)

    return fence_price


def part1() -> int:
    garden_plots = read_file()
    unique_regions = find_all_unique_regions(garden_plots)
    fence_price = calc_fence_price(unique_regions, "Part1")

    return fence_price


def part2() -> int:
    garden_plots = read_file()
    unique_regions = find_all_unique_regions(garden_plots)
    fence_price = calc_fence_price(unique_regions, "Part2")

    return fence_price


if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")
