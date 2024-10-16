class Player:

    def __init__(self, name: str):
        self.name: str = name
        self.balance: int = 0
        self.bet: int = 0
        self.no_hands: int = 1
        self.insurance: bool = False

