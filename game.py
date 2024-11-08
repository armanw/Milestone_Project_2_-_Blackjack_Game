from typing import List
from player import Player
from deck import Deck
from hand import Hand
from renderer import Renderer, Question


class Game:

    def __init__(self):
        self.player1: Player = Player()
        self.dealer_hand: Hand = Hand()

    def run(self):

        Renderer.display_message("Welcome to BlackJack Pro Premium Ultra Ubuntu 9.4 (early access)")
        name_question = Question(
            question="What's your name?",
            validation_rule=r'[^\s].*',
            error_msg="Wrong input"
        )
        self.player1.name = Renderer.ask_question(name_question)
        self.player1.balance = 50
        playing_deck = Deck()

        bet_question = Question(
            question="How much you wanna bet?",
            validation_rule=r'\d+',
            error_msg="Bet amount should be a number"
        )
        bet_amount = int(Renderer.ask_question(bet_question))

        while not self.player1.can_afford_bet(bet_amount):
            Renderer.display_message(f"You cannot afford that bet. Your balance is {self.player1.balance}")
            bet_amount = int(Renderer.ask_question(bet_question))

        self.player1.place_bet(bet_amount)