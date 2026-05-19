available_parts = {
    "1": "Computer",
    "2": "Monitor",
    "3": "Keyboard",
    "4": "Mouse",
    "5": "HDMI Cable",
    "6": "DVD Drive",
}
current_choice = "-"
computer_parts = {}

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            print(f"Removing {chosen_part}")
            del computer_parts[current_choice]
        else:
            print(f"Adding: {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"Your dictionary now contains: {computer_parts}")
    else:
        print("Choose an available option:")
        for key, value in available_parts.items():
            print(f"\t{key}: {value}")
        print("\t0: Finish")
    current_choice = input("\t> ")
