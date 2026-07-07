import random

from brain_games.engine import run

DESCRIPTION = 'Find the greates common divisor pf given numbers.'


def get_gcd(first_number, second_number):
    while second_number != 0:
        first_number, second_number = (
            second_number,
            first_number % second_number,
        )
    return first_number


def question_and_answer():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)

    question = f'{first_number} {second_number}'
    correct_answer = str(get_gcd(first_number, second_number))

    return question, correct_answer


def run_game():
    run(DESCRIPTION, question_and_answer)