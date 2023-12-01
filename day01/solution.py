import re

test_input_part01 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

test_input_part02 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

digits_part01 = {str(i): str(i) for i in range(1, 10)}

word2digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
digits_part02 = digits_part01 | word2digit


def calibration_sum(lines: list[str], digits: dict[str, str]) -> int:
    pattern = re.compile("(?=(" + r"|".join(digits) + "))")

    values = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        matches = pattern.findall(line)
        first_digit, last_digit = matches[0], matches[-1]
        values.append(int(digits[first_digit] + digits[last_digit]))

    return sum(values)


def tests() -> None:
    v = calibration_sum(test_input_part01.splitlines(), digits_part01)
    print(v)
    v = calibration_sum(test_input_part02.splitlines(), digits_part02)
    print(v)


def main() -> None:
    with open("input.txt") as f:
        lines = f.readlines()

    v = calibration_sum(lines, digits_part01)
    print(v)
    v = calibration_sum(lines, digits_part02)
    print(v)


if __name__ == "__main__":
    main()
