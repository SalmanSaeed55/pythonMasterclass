computer_parts = ["Computer", "Monitor", "Keyboard", "Mouse", "Mouse pad"]

for part in computer_parts:
    print(part)

print()

print(computer_parts[3])
print(computer_parts[0])
print(computer_parts[-1])

print(computer_parts[0:3])

even = [2, 4 , 6, 8]
odd = [3, 5, 7, 9]

print(len(even))
print(min(even))
print(max(even))

even.append(10)
print(even)

print(len(odd))
print(min(odd))
print(max(odd))

odd.append(11)
print(odd)

print()

s = "Mississippi"
print(s.count("s"))

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

digits = list("3648273284580")
print(digits)

more_numbers = list(numbers)
print(more_numbers)

print(numbers is more_numbers)

computer_parts = ["Keyboard", "Mouse", "Monitor", "Computer"]
print(computer_parts)
computer_parts[3] = "Mouse Pad"
print(computer_parts)