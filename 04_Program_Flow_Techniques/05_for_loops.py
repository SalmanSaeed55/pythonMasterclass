parrot  = "Norwegian Blue"

for letter in parrot:
    print(letter)

number = "1,234,474;493,138.348/384 232,232,453"
separators = ""
values = []

for char in number:
    if not char.isnumeric():
        separators += char
    else:
        values.append(int(char))

print(separators)
print(sum(values))