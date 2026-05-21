small_ints = set(range(21))
print(small_ints)

small_ints.clear()
print(small_ints)

more_ints = set(range(21))
more_ints.discard(3)
more_ints.remove(2)
print(more_ints)

print("-" * 100)

travel_mode = {"1": "car", "2": "plane"}

items = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier",
}

restricted_items = {
    "catapult",
    "fuel",
    "gun",
    "knife",
    "razor blades",
    "scissors",
    "shampoo",
}

print("Please choose your mode of travel:")
for key, value in travel_mode.items():
    print(f"{key}: {value}")

mode = "-"
while mode not in travel_mode:
    mode = input("> ")

if mode == "2":
    # traveling by plane, remove restricted items
    for restricted_item in restricted_items:
        items.discard(restricted_item)

print("You need to pack:")
for item in sorted(items):
    print(item)

print("-" * 100)

patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}

while patients:
    patient = patients.pop()
    print(f"{patient}")
