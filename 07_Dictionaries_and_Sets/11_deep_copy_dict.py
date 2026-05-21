import copy

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"]
}

things = copy.deepcopy(animals)

print(things["teddy"])
print(animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])