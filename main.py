
from deck import Deck
import itertools

if __name__ == "__main__":

    # new_deck = Deck(1)
    # print(new_deck)
    #
    # print(new_deck.deal(60))
    # print(new_deck)

    a = [5]
    b = [1,11]
    c = [1,11]
    d = [8]
    e = [a,b,c,d]
    z = list(itertools.product(*e))
    y = []
    for item in z:
        y.append(sum(item))

    print(list(set(y)))

