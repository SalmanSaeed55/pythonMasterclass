low = 1
high = 1000
guesses = 1

print(f"Please think of a number between {low} and {high}")

while low != high:
    print(f"Guessing between the range:\t{low}\t--->\t{high}")
    guess = low + (high - low) // 2

    print(f"My guess is {guess}")
    feedback = input("Should I guess higher (H), lower (L), or am I correct (C) ").upper()

    if feedback == 'C':
        print(f"I guessed your number in {guesses} guesses!")
        break
    elif feedback == 'H':
        low = guess + 1
    elif feedback == 'L':
        high = guess - 1
    else:
        print("Invalid input. Please enter H, L, or C.")
        continue

    guesses += 1
else:
    print(f"Your number is {low}.\nI guessed it in {guesses} guesses!")
