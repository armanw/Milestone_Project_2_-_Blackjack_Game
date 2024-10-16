import re
# regex


class Decision:

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
    def ask_question(asked_question: Decision) -> str:
        answer = input(asked_question.question)

        while not asked_question.validate(answer):
            # while asked_question...== FALSE
            print(asked_question.error_msg)
            answer = input(asked_question.question)

        return answer.lower()
