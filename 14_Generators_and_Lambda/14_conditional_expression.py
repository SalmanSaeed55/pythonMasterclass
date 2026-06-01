name = input("What is your name? ")
age = int(input("What is your age? "))

print("You are old enough to vote" if age >= 18 else f"Come back in {18 - age} years")
