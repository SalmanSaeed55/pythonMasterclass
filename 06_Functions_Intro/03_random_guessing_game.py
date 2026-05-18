import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin)

    The function will continue looping and prompting until the user enters a valid `int`

    :param prompt: The string that the user will see when they're promted to enter a value
    :return: The integer that the user enters
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print(f"{temp} is not a valid guess. Try again.")


answer = random.randint(1, 20)
guess = 0
guesses = 0
print(answer)  # TODO: remove after testing

while guess != answer:
    guess = get_integer("Guess a number between 1 and 20: ")

    if guess == 0:
        print("Exiting the game. Goodbye!")
        break

    if guess < answer:
        print("Too low, try again.")
        guesses += 1
    elif guess > answer:
        print("Too high, try again.")
        guesses += 1
    else:
        print(f"Congratulations! You guessed the number in {guesses + 1} guesses")
