def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

try:
    print(factorial(900))
    print(factorial(1000))
except RecursionError:
    print("The factorial function exceeded the maximum recursion depth.")

print("Program is terminating.")
