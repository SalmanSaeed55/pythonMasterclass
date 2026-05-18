def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def sentence_palindrome(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


word = input("Enter a sentence: ")
if sentence_palindrome(word):
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome")
