vehicles = {
    'Dream': 'Honda 250T',
    'Roadster': 'BMW R1100',
    'ER5': 'Kawasaki ER5',
    'Can-Am': 'Bombardier Can-Am 250',
    'Virago': 'Yamaha XV250',
    'Tenere': 'Yamaha XT650',
    'Jimmy': 'Suzuki Jimmy 1.5',
    'Fiesta': 'Ford Fiesta Ghia 1.4'
}

vehicles["Starfighter"] = "Lockhead F-104"
vehicles["Learjet"] = "Bombardier Learjet 75"
vehicles["Toy"] = "Glider"

for key, value in vehicles.items():
    print(key, value, sep=", ")

print()

# Upgrade Virago
vehicles["Virago"] = "Yamaha XV535"

for key, value in vehicles.items():
    print(key, value, sep=", ")

# Deleting Entries from a Dictionary
print()
del vehicles["Starfighter"]

for key, value in vehicles.items():
    print(key, value, sep=", ")