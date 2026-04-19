print("Today is a good day to learn Python")
print('Python is fun')

print("Python's string are easy to use")
print('Python\'s string are easy to use') # escaping the character out
print('"Here is a quote"')

print("Hello " + "World") # concatenation
greeting = "Hello"
name = "Salman"
print(greeting + " " + name) # Space is necessary

name = input("What is your name? ")
print("Hello " + name + ", welcome to Python programming!")


parrot = "Norwegian Blue"
print(parrot)
print(parrot[3]) # prints out "w" as indexing starts at 0

print(parrot[3:5])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-1]) # negative indexes start at -1 as -0 just isn't a thing
print(parrot[-14])

print()

# SLICING
    # [Start:Stop:Step]

print(parrot[0:6])
print(parrot[3:5])
print(parrot[:9])
print(parrot[10:])

print()

letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[::2])
print(letters[:12:3])
print(letters[12::3])
print(letters[::-1])
