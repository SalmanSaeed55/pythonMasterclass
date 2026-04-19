option = None

while option not in range(10):
    option = int(input("Please select an option:\n\t1. Learn Python\n\t2. Go Swimming\n\t3. Do some work\n\t4. Go to the gym\n\t5. Go out with friends\n\t6. Watch a movie\n\t7. Read a book\n\t8. Take a nap\n\t9. Go for a walk\n\t0. Exit\n"))

    if option == 0:
        print("Exiting the program. Goodbye!")
        break
else:
    print(f"You selected option {option}. Enjoy your activity!")