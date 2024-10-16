from typing import List


class Card:
    POSSIBLE_COLORS = [
        "\u2660",  # Spades
        "\u2665",  # hearts
        "\u2666",  # Diamond
        "\u2663"  # club
    ]
    POSSIBLE_RANKS = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

    def __init__(self, color: str, rank: str, points: List[int]):
        self.color: str = color
        self.rank: str = rank
        self.points: List[int] = points

    def __repr__(self):
        return f"{self.rank}{self.color}"

    def __str__(self):
        return f"{self.rank}{self.color}"