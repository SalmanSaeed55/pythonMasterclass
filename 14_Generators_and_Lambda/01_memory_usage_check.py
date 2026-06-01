import sys

def my_range(n:int):
    print("my_range start")
    start = 0
    while start < n:
        print("my_range is returning", start)
        yield start
        start += 1

_ = input("line 11")
big_range = my_range(5)

_ = input("line 15")

print(f"big_range: {sys.getsizeof(big_range)} bytes")

big_list = []

_ = input("line 17")
for val in big_range:
    _ = input("line 22 inside loop")
    big_list.append(val)

print(f"big_list: {sys.getsizeof(big_list)} bytes")


print(big_range)
print(big_list)