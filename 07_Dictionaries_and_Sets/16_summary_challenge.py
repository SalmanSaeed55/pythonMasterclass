choice = "-"

while choice != "0":
    if choice in {"1", "2", "3", "4", "5"}:
        print(f"You chose {choice}")
    else:
        print(f"Please choose your options from the list below:")
        print("""1:\t Learn Python
                    2:\t Learn JavaScript
                    3:\t Go swimming
                    4:\t Have Dinner
                    6:\t Go to sleep
                    0:\t Exit""")
    choice = input("Please choose your option: ")