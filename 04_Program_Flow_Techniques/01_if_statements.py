name = input("Please enter your name: ")
age = int(input(f"Please enter your age, {name}: "))
print(age)

if age >= 18:
    print(f"{name}, you are old enough to vote")
    print("Please put an X in the box")
else:
    print(f"{name}, come back in {18 - age} years")

# alternate method
if age < 18:
    print(f"{name}, come back in {18 - age} years")
elif age == 900:
    print("Sorry Yoda. You die in the Return of the Jedi")
else:
    print(f"{name}, you are old enough to vote")
    print("Please put an X in the box")