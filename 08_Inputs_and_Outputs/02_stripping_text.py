file = "./files/Jabberwocky.txt"

with open(file) as poem:
    first  = poem.readline().rstrip()

print(first)

chars = "' Twasebv"
no_apostrophe = first.strip(chars)
print(no_apostrophe)

print("-" * 80)

twas_removed = first.removeprefix("'Twas")
print(twas_removed)
toves_removed  = first.removesuffix("toves")
print(toves_removed)