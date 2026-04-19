name = input("Please enter your name:\t")
age = int(input("Please enter your age:\t"))

if name:
    if 18 <= age <= 30:
        print(f"You are within the age range for the trip!\nWelcome aboard, {name}!")
    elif age < 18:
        print("Sorry, you are too young for the trip.")
    else:
        print("Sorry, you are too old for the trip.")
else:
    print("Sorry, you must enter your name to proceed.")