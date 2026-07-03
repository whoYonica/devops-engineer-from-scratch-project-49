import random


from brain_games.engine import run


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def answer_and_question():
    number = random.randint(1, 100)

    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'

    return question, correct_answer


def run_game():
    run(DESCRIPTION, answer_and_question)