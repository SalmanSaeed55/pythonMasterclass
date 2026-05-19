from contents import pantry, recipes

# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dict = {}

for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    print("Please choose your recipe:")
    print("-" * 20)
    for key, value in display_dict.items():
        print(f"{key}. {value}")

    choice = input("\t> ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected: {selected_item}")
        print("Checking pantry...")
        ingredients = recipes[selected_item]
        print(f"\t{ingredients}")