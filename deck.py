import cards
import random

class NotEnoughCardsException(Exception):
    pass

class Deck:

    def __init__(self, decks_amount: int = 1):
        self.cards_deck = []

        for amount in range(decks_amount):
            for color in cards.Card.POSSIBLE_COLORS:
                for rank in cards.Card.POSSIBLE_RANKS:

                    # assign point accordingly to rank
                    if rank.isnumeric():
                        points = [int(rank)]
                    elif rank == "A":
                        points = [11, 1]
                    else:
                        points = [10]

                    card = cards.Card(color, rank, points)
                    self.cards_deck.append(card)

        self.deck_shuffle()

    def deck_shuffle(self):
        random.shuffle(self.cards_deck)

    def __repr__(self):
        return ", ".join([str(card) for card in self.cards_deck])

    def deal(self, cards_amount: int = 1):
        if len(self.cards_deck) < cards_amount:
            raise NotEnoughCardsException
        else:
            return [self.cards_deck.pop() for _ in range(cards_amount)]


