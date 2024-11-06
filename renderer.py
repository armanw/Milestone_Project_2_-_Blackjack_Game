import re
from hand import Hand
# regex


class Question:

    def __init__(self, question: str, validation_rule: str, error_msg: str):
        self.question = question
        # Is Earth flat?
        self.validation_rule = validation_rule
        # [ynYN]
        self.error_msg = error_msg
        # 'Can you write...?'

    def validate(self, user_input: str) -> bool:
        match = re.match(self.validation_rule, user_input)
        return match is not None


class Renderer:

    @staticmethod
    def display_message(message: str):
        print(message)

    @staticmethod
    def ask_question(asked_question: Question) -> str:
        answer = input(asked_question.question)

        while not asked_question.validate(answer):
            # while asked_question...== FALSE
            print(asked_question.error_msg)
            answer = input(asked_question.question)

        return answer.lower()

    @staticmethod
    def display_full_hand(hand: Hand):
        # show cards on hand
        print(hand.hand_deck)

    @staticmethod
    def display_first_card(hand: Hand):
        print(hand.hand_deck[0])

    @staticmethod
    def display_hand_points(hand: Hand):
        print(hand.get_hand_values())
