a = b = c = d = e = f = 12
print(f)

x, y = 1, 2
print(x, y)

print("Unpacking tuples")
data = (1, 2, 76)

x, y, z = data
print(x)
print(y)
print(z)

data = [23, 24, 25]
x, y, z = data
print(x)
print(y)
print(z)

welcome = ("Welcome to my nightmare", "Alice Cooper", 1975)
bad = ("Bad Company", "Bad Company", 1974)
budgie = ("Nightflight", "Budgie", 1981)
imelda = ("More Mayhem", "Emilda May", 2011)
metallica = ("Ride the Lightening", "Metallica", 1984)

title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ("Coffee table", 200, 100, 75, 34.50)

name, length, width, height, price = table
print(length * width)

print()

albums = [
    ("Welcome to my nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightening", "Metallica", 1984)
]

print(len(albums))

for album in albums:
    name, artist, year = album
    print(f"Album: {name}, Artist: {artist}, Year: {year}")

# Another way
print()
for name, artist, year in albums:
    print(f"Album: {name}, Artist: {artist}, Year: {year}")