current_choice = "-"
computer_parts = []
available_part  = ["Computer", "Monitor", "Keyboard", "Mouse", "Printer", "HDMI Cable", "DVD Drive"]
# valid_choices = [str(i) for i in range(len(computer_parts) + 1)]
valid_choices = []
for i in range(len(available_part) + 1):
    valid_choices.append(str(i))

while current_choice != "0":
    if current_choice in valid_choices:
        selected_part = available_part[int(current_choice) - 1]
        if selected_part in computer_parts:
            print(f"Removing {selected_part} from the list.")
            computer_parts.remove(selected_part)
        else:
            print(f"Adding {selected_part} to the list.")
            computer_parts.append(selected_part)
        print(f"Your list now contains {computer_parts}")
    else:
        print("Please add options from the list below:")
        for i, part in enumerate(available_part):
            print(f"{i + 1}: {part}")
    current_choice = input("> ")

print(computer_parts)