import random

from brain_games.engine import run

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def question_and_answer():
    number = random.randint(1, 100)

    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'

    return question, correct_answer


def run_game():
    run(DESCRIPTION, question_and_answer)