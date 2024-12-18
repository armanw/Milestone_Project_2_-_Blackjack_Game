from typing import List

import player
from player import Player
from deck import Deck
from hand import Hand, HandStatus
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
        if any([x==21 for x in self.dealer_hand.get_hand_values()]):
            self.dealer_hand.status = HandStatus.BLACKJACK
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
                self.player1.balance -= 0.5 * self.player1.bet

        self.player1.hands[0] = Hand() #adding player's first hand
        self.player1.hands[0].add_cards(playing_deck.deal(2)) #giving 2 cards
        if any([x==21 for x in self.player1.hands[0].get_hand_values()]):
            self.player1.hands[0].status = HandStatus.BLACKJACK
            #if first deal is blackjack then status is blackjack
        Renderer.display_full_hand(self.player1.hands[0]) # show cards

            # uncomment for TEST FOR SPLIT
        #matching = True
        #if matching:

        if self.player1.hands[0].has_matching_cards():
            if Renderer.ask_question(split_question).lower() == "y":
                self.player1.split_cards(playing_deck.deal(2))


        hit_or_stand_question = Question(
            question="Would you like to HIT or STAND? Type H or S: ",
            validation_rule=r'[hHsS]',
            error_msg="Type H for Hit or S for stand"
        )

        for hand in self.player1.hands:

            if hand.status != HandStatus.IN_PLAY:
                continue #if true, next iteration
            # Renderer.display_full_hand(hand)

            next_action = Renderer.ask_question(hit_or_stand_question)
            while next_action == 'h' and hand.status == HandStatus.IN_PLAY:
                hand.add_cards(playing_deck.deal())

                if any([x==21 for x in hand.get_hand_values()]):
                    hand.status = HandStatus.TWENTY_ONE
                elif all([x>21 for x in hand.get_hand_values()]):
                    hand.status = HandStatus.LOST
                else:
                    Renderer.display_full_hand(hand)
                    next_action = Renderer.ask_question(hit_or_stand_question)

            if next_action == 's':
                hand.status = HandStatus.STAND

            # Renderer.display_message(str(hand.status)) # FOR TEST!!!

        #if dealer already has blackjack, below has no effect
        while any([x<17 for x in self.dealer_hand.get_hand_values()]):
            self.dealer_hand.add_cards(playing_deck.deal())
            if any([x == 21 for x in self.dealer_hand.get_hand_values()]):
                self.dealer_hand.status = HandStatus.TWENTY_ONE
            elif all([x > 21 for x in self.dealer_hand.get_hand_values()]):
                self.dealer_hand.status = HandStatus.LOST

        if self.dealer_hand.status == HandStatus.IN_PLAY:
            self.dealer_hand.status = HandStatus.STAND

        for hand in self.player1.hands:
            if (hand.status == HandStatus.STAND) and (self.dealer_hand.status == HandStatus.STAND):
                player_max = max([x for x in hand.get_hand_values() if x<=21])
                dealer_max = max([x for x in self.dealer_hand.get_hand_values() if x<=21])

                if player_max > dealer_max:
                    Renderer.display_message("Congrats, you won!")
                    self.player1.balance += self.player1.bet
                    if hand.status == HandStatus.BLACKJACK:
                        self.player1.balance += 0.5 * self.player1.bet

                elif player_max == dealer_max:
                    Renderer.display_message("Tie!")

                else:
                    Renderer.display_message("you lost XD!")


            elif hand.status.value > self.dealer_hand.status.value:
                Renderer.display_message("Congrats, you won!")
                self.player1.balance += self.player1.bet
                if hand.status == HandStatus.BLACKJACK:
                    self.player1.balance += 0.5 * self.player1.bet

            elif hand.status.value == self.dealer_hand.status.value:
                Renderer.display_message("Tie!")
            else:
                Renderer.display_message("you lost XD!")

        if self.player1.insurance and self.dealer_hand.status == HandStatus.BLACKJACK:
            self.player1.balance += 2*0.5 * self.player1.bet

        Renderer.display_message(f"Your current balance is: {self.player1.balance}")
