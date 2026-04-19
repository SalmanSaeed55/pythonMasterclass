for i in range(1, 21):
    print(f"i is now {i}")

print("-" * 80)

for i in range(10):
    print(i)

print("-" * 80)

for i in range(0, 10, 2):
    print(i)

age = int(input("Please enter your age: "))

if age in range(16, 66):
    print("You are of working age.")
else:
    print("You are not of working age.")

for i in range(1, 13):
    for j in range(1, 13):
        print(f"{i} x {j} = {i * j}")
    print("-" * 20)