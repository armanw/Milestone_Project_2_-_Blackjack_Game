from deck import Deck
from player import Player
from renderer import Renderer

if __name__ == "__main__":

    new_deck = Deck(1)
    print(new_deck)

    Zbysiu = Player("Zbysiu")
    Zbysiu.hands[0].add_cards(new_deck.deal(2))
    Renderer.display_full_hand(Zbysiu.hands[0])
    Renderer.display_hand_points(Zbysiu.hands[0])
    Renderer.display_first_card(Zbysiu.hands[0])

    Zbysiu.split_cards(new_deck.deal(2))
    Renderer.display_full_hand(Zbysiu.hands[0])
    Renderer.display_full_hand(Zbysiu.hands[1])
