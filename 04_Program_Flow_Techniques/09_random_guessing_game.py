import random

answer = random.randint(1, 20)
guess = 0
guesses = 0
print(answer) # TODO: remove after testing

while guess != answer:
    guess = int(input("Guess a number between 1 and 20: "))

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