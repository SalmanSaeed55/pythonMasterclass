data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

plants_filepath = "./files/flowers_write.txt"

# with open(plants_filepath, "w") as plants:
#     for plant in data:
#         plants.write(plant)
#
# print(data)

filename = "./files/test_numbers.txt"

with open(filename, "w") as test:
    for i in range(10):
        print(i, file=test)

with open(filename, "w") as test:
    for i in range(10):
        test.write(str(i) + "\n")
