test_input = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


def parse_lines(lines: list[str]) -> list[tuple[list[str], list[str]]]:
    splits = [line.split("|") for line in lines]
    return [
        (winning_numbers.split(":")[1].split(), numbers.split())
        for winning_numbers, numbers in splits
    ]


def worth_of_scratch_cards(scratch_cards: list[tuple[list[str], list[str]]]) -> int:
    matches = {
        card_number: len(set(scratch_numbers) & set(winning_numbers))
        for card_number, (winning_numbers, scratch_numbers) in enumerate(
            scratch_cards, start=1
        )
    }
    return sum(int(2 ** (i - 1)) for i in matches.values())


def total_scratch_cards(scratch_cards: list[tuple[list[str], list[str]]]) -> int:
    """
    Example for test_input:
    1: 1
    2: 1 + =>1 1 = 2
    3: 1 + =>1 1 + (=>2 1 + 1) = 4
    4: 1 + =>1 1 + (=>2 1 + 1) + (=>3 1 + 1 + (1 + 1)) = 8
    5: 1 + =>1 1 + (=>3 1 + 1 + (1 + 1)) + (=>4 1 + 1 + (1 + 1) + (1 + 1 + (1 + 1))) = 14
    6: 1
    """
    matches = {}
    scores = {card_number: 1 for card_number in range(1, len(scratch_cards) + 1)}
    for card_number, (winning_numbers, scratch_numbers) in enumerate(
        scratch_cards, start=1
    ):
        matches[card_number] = len(set(scratch_numbers) & set(winning_numbers))
        for card_copy in range(card_number + 1, card_number + matches[card_number] + 1):
            scores[card_copy] += scores[card_number]
    return sum(scores.values())


def main() -> None:
    import os

    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    scratch_cards = parse_lines(test_input.strip().splitlines())
    assert worth_of_scratch_cards(scratch_cards) == 13
    assert total_scratch_cards(scratch_cards) == 30

    with open(input_file) as f:
        lines = f.read().strip().splitlines()
    scratch_cards = parse_lines(lines)
    print(worth_of_scratch_cards(scratch_cards))  # 20117
    print(total_scratch_cards(scratch_cards))  # 13768818


if __name__ == "__main__":
    main()
