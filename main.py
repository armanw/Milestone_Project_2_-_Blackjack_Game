
from deck import Deck
import itertools
from hand import Hand
from player import Player

if __name__ == "__main__":

    new_deck = Deck(1)
    print(new_deck)

    Zbysiu = Player("Zbysiu")
    Zbysiu.hands[0].add_cards(new_deck.deal(2))
    print(Zbysiu.hands[0].hand_deck)
    print(Zbysiu.hands[0].get_hand_values())




