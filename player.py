from typing import List
from hand import Hand


class Player:

    def __init__(self, name: str):
        self.name: str = name
        self.balance: int = 0
        self.bet: int = 0
        self.hands: List[Hand] = [Hand()]
        self.insurance: bool = False

    def split_cards(self, cards: List):
        # add new hand
        self.hands.append(Hand())
        # pop card from one hand, add to another
        self.hands[1].add_cards([self.hands[0].hand_deck.pop()])

        self.hands[0].add_cards([cards[0]])
        self.hands[1].add_cards([cards[1]])

