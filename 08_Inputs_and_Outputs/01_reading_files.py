# jabber = open("./files/Jabberwocky.txt", "r")
#
# for line in jabber:
#     print(line.rstrip())
#     # print(len(line))
#
# jabber.close()

with open("./files/Jabberwocky.txt", "r") as jabber:
    # for line in jabber:
    #     print(line.rstrip())

    lines = jabber.readlines() # list of lines in the file

print(lines)
print(lines[-1:])
print(*lines[::-1])

with open("./files/Jabberwocky.txt", "r") as jabber:
    lines = jabber.read() # the entire file as a list

print(lines)
for character in reversed(lines):
    print(character, end="")


with open("./files/Jabberwocky.txt", "r") as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if "jubjub" in line.casefold():
            break