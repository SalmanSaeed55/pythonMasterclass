import json

languages = [
    ("ABC", 1987),
    ("Algol 68", 1968),
    ("APL", 1962),
    ("C", 1973),
    ("Haskell", 1990),
    ("Lisp", 1958),
    ("Modula-2", 1977),
    ("Perl", 1987),
]

with open("./files/test.json", "w", encoding="utf-8") as test:
    json.dump(languages, test)

with open("./files/test.json", "r", encoding="utf-8") as test_file:
    data = json.load(test_file)
print(data)
print(data[2])