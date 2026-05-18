def fizz_buzz(number: int) -> str:
    """Take in a number as `int` and returns `str` as 'fizz' or 'buzz' or 'fizz buzz' if the number is divisible by
    3, 5 or both respectively.

    If the number is not divisible by either 3 or 5, return the number as a string.

    :param number: the number to return either fizz or buzz
    :return: `str` either 'fizz', 'buzz', 'fizz buzz' or the number as a string
    """
    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


input("Play Fizz Buzz! Press enter to start.")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))

    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your turn")

    if players_answer != correct_answer:
        print(f"Wrong! The correct answer was {correct_answer}.")
        break
else:
    print("Congratulations! You made it to 99 without a mistake!")