three_ints = input("Enter 3 integers, seperated by ','")

integers = three_ints.split(",")
a = int(integers[0])
b = int(integers[1])
c = int(integers[2])

print(a + b - c)