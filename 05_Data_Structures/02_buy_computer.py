current_choice = "-"
computer_parts = []
available_part  = ["Computer", "Monitor", "Keyboard", "Mouse", "Printer", "HDMI Cable", "DVD Drive"]
# valid_choices = [str(i) for i in range(len(computer_parts) + 1)]
valid_choices = []
for i in range(len(available_part) + 1):
    valid_choices.append(str(i))

while current_choice != "0":
    if current_choice in valid_choices:
        print(f"Adding {available_part[int(current_choice) - 1]} to the list.")
        computer_parts.append(available_part[int(current_choice) - 1])
    else:
        print("Please add options from the list below:")
        for i, part in enumerate(available_part):
            print(f"{i + 1}: {part}")
    current_choice = input("> ")

print(computer_parts)