def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = previous + current, current

fib = fibonacci()
for _ in range(10):
    print(next(fib))