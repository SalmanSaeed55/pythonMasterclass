def sum_numbers(*numbers: float)-> float:
    """
    Takes in a sequence of numbers and sums them together
    :param numbers: The sequence of numbers to be added
    :return: prints out the sum of numbers, or returns `None`
    """
    return sum(numbers)


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
