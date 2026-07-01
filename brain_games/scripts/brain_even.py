import prompt


import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_even(number)->bool:
    if number % 2 == 0:
        return True
    else:
        return False


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')


        answer = prompt.string("Your answer: ")
        correct_answer = "yes" if is_even(random_number) else "no"
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
    

if __name__ == '__main__':
    main()