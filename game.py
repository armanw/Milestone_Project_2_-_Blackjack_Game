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
        Renderer.display_message("Let's start the game!")
        #dealer's turn
        self.dealer_hand.add_cards(playing_deck.deal(2))
        Renderer.display_message("Dealer's first card: ")
        Renderer.display_first_card(self.dealer_hand)

        insurance_question = Question(
            question="Would you like to take insurance? Y/N?",
            validation_rule=r'[yYnN]',
            error_msg="Type Y for yes and N for no"
        )
        split_question = Question(
            question="Would you like to split the hand? Y/N",
            validation_rule=r'[yYnN]',
            error_msg="Type Y for yes and N for no"
        )
        stand_question = Question(
            question="Would you like to stand? Y/N",
            validation_rule=r'[yYnN]',
            error_msg="Type Y for yes and N for no"
        )

        #getting to dealer's first card's rank
        dealer_1card_rank = self.dealer_hand.hand_deck[0].rank #assigned to var, cuz me can
        #dealer_1card_rank = "A" # FOR TESTING
        if dealer_1card_rank == "A":
            Renderer.display_message(
                f"Dealer's first card's rank is: {dealer_1card_rank}, "
                f"do you want to place insurance?") # looks stupid, but clear communication is good
            wants_insurance = Renderer.ask_question(insurance_question).lower()

            if wants_insurance == "y":
                self.player1.insurance = True
                # no money here, cuz it's always 50%

        self.player1.hands[0] = Hand() #adding player's first hand
        self.player1.hands[0].add_cards(playing_deck.deal(2)) #giving 2 cards
        Renderer.display_full_hand(self.player1.hands[0]) # show cards

            # uncomment for TEST FOR SPLIT
        #matching = True
        #if matching:

        if self.player1.hands[0].has_matching_cards():
            if Renderer.ask_question(split_question).lower() == "y":
                self.player1.split_cards(playing_deck.deal(2))
                #print("i;m here")
        #placeholder for split, for now there is only one hand

        # TO DO: find a way to display all hands or something, if there is one hand it throws error
        #Renderer.display_full_hand(self.player1.hands[0])
        #Renderer.display_full_hand(self.player1.hands[1]) # FOR TESTING SPLIT


