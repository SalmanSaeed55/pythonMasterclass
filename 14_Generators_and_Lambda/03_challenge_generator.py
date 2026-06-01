def odd():
    start = 1
    while True:
        yield start
        start += 2


def pi_series():
    odds = odd()
    approx  =0
    while True:
        approx += (4 / next(odds))
        yield approx
        approx -= (4 / next(odds))
        yield approx

# odds = odd()

approx_pi = pi_series()

for _ in range(2000000):
    print(next(approx_pi))