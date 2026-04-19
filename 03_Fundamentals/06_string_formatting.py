for i in range(1, 13):
    print(f"{i:2} squared is {i**2:3} and cubed is {i**3:4}")

print()

for i in range(1, 13):
    print(f"{i:2} squared is {i**2:<3} and cubed is {i**3:<4}")

print(f"Pi is approximately {22 / 7:12.2f}") # precision is more important than field width
print(f"Pi is approximately {22 / 7:12}")

