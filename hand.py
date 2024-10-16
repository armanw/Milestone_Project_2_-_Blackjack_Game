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
        values = []
        for card in self.hand_deck:
            for points in card.points:
                values[0] = values[0] + points

        for card in self.hand_deck:
            if card.rank == "A":
                pass
                # values [a, b, b]
                # values [a+1+1, a+11+1, a+11+11]
                # [13, 3]
                # [11,1]
                # [14, 4, 24, 14]
                # [2]
                # [16, 6, 26, 16]
                # [11,1]
                # [16, 6, 26, 16]
                #
                # 1,2

            # else
            #     for values
            #         + points



