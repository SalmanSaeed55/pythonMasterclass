# numbers = {*""} - an ugly way to initialise an empty set
# numbers = {*{}} - another ugly way to initialise an empty set
numbers = set()

print(type(numbers), numbers)

# numbers.add(1)
# print(numbers)

while len(numbers) < 4:
    next_value = int(input("Please enter a number: "))
    numbers.add(next_value)

for i in range(4):
    print(numbers)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]
unique_colours = sorted(set(data))
print(unique_colours)
