numbers = (0, 1, 2, 3, 4, 5)

print(numbers, sep=";")
print(*numbers, sep=";")
print(1, 2, 3, 4, 5, sep=";")

name = "Salman"
print(*name, sep=";")


def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(1, 2, 3, 4, 5, 6)

print()
test_star()