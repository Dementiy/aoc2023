from math import prod

test_input = """
Time:      7  15   30
Distance:  9  40  200
"""


def parse_lines(lines: list[str]) -> tuple[list[int], list[int]]:
    time_line, distance_line = lines
    times = [int(v) for v in time_line.strip("Time:").split()]
    distances = [int(v) for v in distance_line.strip("Distance:").split()]
    return times, distances


def get_number_of_ways(time: int, distance: int) -> int:
    return sum(((time - step) * step) > distance for step in range(1, time))


def part01(times: list[int], distances: list[int]) -> int:
    return prod(get_number_of_ways(time, dist) for time, dist in zip(times, distances))


def part02(time: int, distance: int) -> int:
    # TODO: Use binary search
    return get_number_of_ways(time, distance)


if __name__ == "__main__":
    import os

    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file) as f:
        lines = f.read().strip().splitlines()

    times, distances = parse_lines(test_input.strip().splitlines())
    time = int("".join(str(t) for t in times))
    dist = int("".join(str(d) for d in distances))
    assert part01(times, distances) == 288
    assert part02(time, dist) == 71503

    times, distances = parse_lines(lines)
    time = int("".join(str(t) for t in times))
    dist = int("".join(str(d) for d in distances))
    print(part01(times, distances))  # 2612736
    print(part02(time, dist))  # 29891250
