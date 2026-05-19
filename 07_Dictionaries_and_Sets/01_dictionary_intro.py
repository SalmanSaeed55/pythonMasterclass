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

my_car = vehicles['Fiesta']
print(my_car)

commuter = vehicles['Virago']
print(commuter)

learner = vehicles.get('ER5')
print(learner)

print()

for key in vehicles:
    print(key, vehicles[key], sep=':\t')

print()

for key, value in vehicles.items():
    print(key, value, sep=':\t')