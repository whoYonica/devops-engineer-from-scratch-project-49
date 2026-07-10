import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(first, second):
    while second != 0:
        first, second = second, first % second
    return first


def question_and_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)

    question = f'{number1} {number2}'
    correct_answer = str(gcd(number1, number2))

    return question, correct_answer