odd = [1, 3, 5, 7, 9, 11, 13]
even = [2, 4, 6, 8, 10, 12, 14, 16]

even.extend(odd)
print(even)

another_even = even
print(another_even)

even.sort()
print(even)

even.sort(reverse = True)
print(even)

print(another_even)

pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3, 1.5, 4.7, 3.2, 0.8]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

print("-" * 100)

# Case Insensitive Sorting
pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram, key = str.casefold)
print(letters)

names = ["Terry", "John", "Jerry", "Micheal", "harry"]
names.sort(key = str.casefold)
print(names)