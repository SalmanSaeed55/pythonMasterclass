def factorial(n:int)->int:
    """
    Calculate the factorial of a given number
    :param n: The number to calculate the factorial
    :return:  of the number
    """
    answer = 1
    for j in range(1, n + 1):
        answer *= j
    return answer

for i in range(1, 36):
    print(f"{i} {factorial(i)}")