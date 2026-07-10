import prompt


from brain_games.cli import welcome_user

ROUNDS = 3


def run(game):
    name = welcome_user()

    print(game.DESCRIPTION)

    for _ in range(ROUNDS):
        question, correct_answer = game.question_and_answer()

        print(f'Question: {question}')

        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')