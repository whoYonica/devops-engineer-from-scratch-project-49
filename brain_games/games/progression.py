import random


from brain_games.engine import run


DESCRIPTION = 'What number is missing in the progression?'

PROGRESSION_LENGTH = 10
MIN_START = 1
MAX_START = 20
MIN_STEP = 1
MAX_STEP = 10


def make_progression(start, step, length):
    progression = []

    for index in range(length):
        progression.append(start + index * step)

    return progression


def question_and_answer():
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)

    progression = make_progression(start, step, PROGRESSION_LENGTH)

    hidden_index = random.randint(0, PROGRESSION_LENGTH - 1)

    correct_answer = str(progression[hidden_index])

    progression[hidden_index] = '..'

    question = ' '.join(map(str, progression))

    return question, correct_answer


def run_game():
    run(DESCRIPTION, question_and_answer)