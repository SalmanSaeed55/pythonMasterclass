print(__file__)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [number ** 2 for number in numbers]

# for number in numbers:
#     squares.append(number ** 2)

print(squares)

text = "what have the romans ever done for us"

capitals = [chars.upper() for chars in text]
print(capitals)
words = [words for words in text.split(" ")]
print(words)