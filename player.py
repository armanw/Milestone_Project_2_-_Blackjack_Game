from typing import List
from hand import Hand


class Player:

    def __init__(self, name: str):
        self.name: str = name
        self.balance: int = 0
        self.bet: int = 0
        self.hands: List[Hand] = [Hand()]
        self.insurance: bool = False

