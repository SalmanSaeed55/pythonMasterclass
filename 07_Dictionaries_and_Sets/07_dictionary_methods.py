d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

d2 = {
    7: "lucky seven",
    10: "ten",
    3: "This is the new three",
}

pantry_items = ["chicken", "spam", "egg", "bread", "lemon"]

new_dict = dict.fromkeys(pantry_items, 0)
print(new_dict)

keys = d.keys()
print(keys)

for item in d:
    print(item)

print()

d.update(d2) # updating a dictionary using another dictionary
for key, value in d.items():
    print(key, value, sep=": ")

print()

d.update(enumerate(pantry_items))
for key, value in d.items():
    print(key, value, sep=": ")