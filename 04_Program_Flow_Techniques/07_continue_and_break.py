shopping_list = ["Milk", "Eggs", "Bread", "Yoghurt", "Jam", "Butter", "Chocolate Spread", "Chicken Legs", "Pasta", "Rice"]

for item in shopping_list:
    if item != "Yoghurt":
        print(f"Buy {item}")

print()

# Can also be done in the following way:
for item in shopping_list:
    if item == "Yoghurt":
        continue # skips that iteration and moves onto the next one
    print(f"Buy {item}")

print()

for item in shopping_list:
    if item == "Yoghurt":
        break # breaks out of the loop and moves on to the next line of code after the loop
    print(f"Buy {item}")
print("Print after the break")

item_to_find = "Chocolate Spread"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

print(f"Item '{item_to_find}' found at index: {found_at}")

item_to_find = "Lobster"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

if found_at is None:
    print(f"Item '{item_to_find}' not found in the shopping list.")
else:
    print(f"Item '{item_to_find}' found at index: {found_at}")
