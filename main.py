from cards import Card

if __name__ == "__main__":
    deck = []

    for color in Card.POSSIBLE_COLORS:
        for rank in Card.POSSIBLE_RANKS:
            points = []

            # assign point accordingly to rank
            if rank.isnumeric():
                points = [int(rank)]
            elif rank == "A":
                points = [11, 1]
            else:
                points = [10]

            card = Card(color, rank, points)
            deck.append(card)

    print(len(deck))
    print(deck)

