import timeit

text = "what have the romans ever done for us"


def capitals():
    capitals_letters = [char.upper() for char in text]
    return capitals_letters


# using map
def map_capital_letters():
    map_capitals = list(map(str.upper, text))
    return map_capitals


def uppercase_words():
    words = [word.upper() for word in text.split()]
    return words


# Use map
def map_uppercase_words():
    map_words = list(map(str.upper, text.split()))
    return map_words


if __name__ == '__main__':
    print(capitals())
    print(map_capital_letters())
    print(uppercase_words())
    print(map_uppercase_words())

    print(timeit.timeit(capitals, number=100000))
    print(timeit.timeit(map_capital_letters, number=100000))
    print(timeit.timeit(uppercase_words, number=100000))
    print(timeit.timeit(map_uppercase_words, number=100000))