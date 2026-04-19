for i in range(10):
    print(f"i is now {i}")

print()

i = 0
while i != 10:
    print(f"i is now {i}")
    i += 1

print()

available_exits = ["North", "East", "South", "West"]

chosen_exit = ""
while chosen_exit.capitalize() not in available_exits:
    chosen_exit = input("Please choose a direction to exit:\t")

    if chosen_exit == "Quit":
        print("Game over!")
        break
else:
    print("Aren't you glad to get out of there?")