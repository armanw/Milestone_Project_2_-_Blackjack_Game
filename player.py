from typing import List
from hand import Hand


class Player:

    def __init__(self, name: str = "NewPlayer"):
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

    def place_bet(self, bet_amount: int):
        self.bet = bet_amount
        self.balance -= bet_amount

    def can_afford_bet(self, bet_amount: int):
        return bet_amount <= self.balance
