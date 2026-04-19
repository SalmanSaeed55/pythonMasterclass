answer = 5

print("Please guess a number between 1-10")
guess = int(input("Enter guess:\t"))

if guess > answer:
    print("Too high")
    guess = int(input())
    if guess == answer:
        print("Congratulations! You got it second time!")
    else:
        print("Sorry you haven't guessed correclty")
elif guess < answer:
    print("Too low")
    guess = int(input())
    if guess == answer:
        print("Congratulations! You got it second time!")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("Congratulations! You got it first time!")

# Alternative method using different comparison operators
if guess != answer:
    if guess > answer:
        print("Too high")
    else:
        print("Too low")
    guess = int(input())
    if guess == answer:
        print("Congratulations! You got it second time!")
    else:
        print("Sorry you haven't guessed correctly")
else:
    print("Congratulations! You got it first time!")