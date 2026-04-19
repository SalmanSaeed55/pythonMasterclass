age = int(input("Please enter your age: "))

if 16 <= age <= 65:
    print("You are of working age.")
else:
    print("You are not of working age.")

day = "Sunday"
temp = 30
raining = True

if day == "Sunday" and temp > 30 or not raining:
    print("Go swimming")
elif temp < 40 and raining:
    print("Go to the cinema")
else:
    print("Go for a walk")

name = input("Please enter your name: ")

if name:
    print(f"Hello, {name}")
else:
    print("Are you a man with no name?")

parrot = "Norwegian Blue"
letter = input("Enter a letter: ")

if letter in parrot:
    print(f"{letter} is found in {parrot}")
else:
    print("I don't need that letter")

activity = input("What activity would you like to do? ")

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")
else:
    print("Perfect!")