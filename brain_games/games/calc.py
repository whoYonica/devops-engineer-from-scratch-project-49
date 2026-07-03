import random


from brain_games.engine import run


DESCRIPTION = "What is the result of the expression?"


def calculate(first_number, second_number, operator):
    match operator:
        case '+':
            return first_number + second_number
        case '-':
            return first_number - second_number
        case '*':
            return first_number * second_number


def question_and_answer():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)

    operator = random.choice(['+', '-', '*'])

    question = f'{first_number} {operator} {second_number}'

    correct_answer = str(
        calculate(first_number, second_number, operator)
    )

    return question, correct_answer


def run_game():
    run(DESCRIPTION, question_and_answer)