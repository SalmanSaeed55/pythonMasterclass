import sys


def getInt(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("That's not a number")
        except EOFError:
            sys.exit(1)
        finally:
            print("The finally clause always executes no matter what")


first_num = getInt("Please enter a number: ")
second_num = getInt("Please enter another number: ")

try:
    print(first_num / second_num)
except ZeroDivisionError:
    print("Division by zero is not possible")
else:
    print("Division performed successfully")