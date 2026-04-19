numbers = [1, 31, 45, 12, 60]

for number in numbers:
    if number % 8 == 0:
        # Reject the list
        print("Rejected")
        break
else:
    print("All numbers are valid")