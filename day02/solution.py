import re
from math import prod

test_input = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


def possible(set: str, bag: dict[str, int]) -> bool:
    for cubes in set.split(","):
        n, color = cubes.split()
        if int(n) > bag[color]:
            return False
    return True


def sum_of_ids(lines: list[str], bag: dict[str, int]) -> int:
    ids_sum = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        game, configurations = line.split(":")
        game_id = int(game.lstrip("Game "))
        for set in configurations.strip().split(";"):
            if not possible(set, bag):
                break
        else:
            ids_sum += game_id
    return ids_sum


def power_of_sets(lines: list[str]) -> int:
    power = 0
    pattern = re.compile("(\d+)\s(red|blue|green)")
    for line in lines:
        line = line.strip()
        if not line:
            continue

        needs = {"red": 0, "green": 0, "blue": 0}
        for n, color in pattern.findall(line):
            needs[color] = max(needs[color], int(n))
        power += prod(needs.values())

    return power


if __name__ == "__main__":
    print(sum_of_ids(test_input.splitlines(), bag={"red": 12, "green": 13, "blue": 14}))
    print(power_of_sets(test_input.splitlines()))  # 2286

    with open("input.txt") as f:
        lines = f.readlines()
        print(sum_of_ids(lines, bag={"red": 12, "green": 13, "blue": 14}))
        print(power_of_sets(lines))  # 56580
