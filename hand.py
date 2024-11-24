import itertools
from enum import Enum
from typing import List
from cards import Card


class HandStatus(Enum):
    # create existing hand's statuses in game
    IN_PLAY = 0,
    LOST = 1,
    STAND = 2,
    TWENTY_ONE = 3
    # assign any value cuz enum class requires it


class Hand:

    def __init__(self):
        self.hand_deck: List = []
        self.status: HandStatus = HandStatus.IN_PLAY

    def add_cards(self, added_cards: List[Card]):
        # extend adds cards from list to hand deck
        # don't use append, it will nest list into list
        self.hand_deck.extend(added_cards)

    def get_hand_values(self):
        # list with all cards values
        values = [card.points for card in self.hand_deck]
        # iloczyn kartezjański:
        all_possibilities = itertools.product(*values)
        all_points = set([sum(item) for item in all_possibilities])
        return all_points

    def has_matching_cards(self):
        return self.hand_deck[0].rank == self.hand_deck[1].rank