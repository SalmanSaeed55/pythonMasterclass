empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [odd, even]
print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)

menu = [["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "bacon", "toast"],
        ["egg", "bacon", "toast", "hash browns"]]

for meal in menu:
    if "sausage" not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        print(f"{meal} has a sausage score of {meal.count('sausage')}")