car = 'subaru'
print("Is car == 'subaru'? I predict true.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict false.")
print(car == 'audi')



autos = ['audi', 'bmw', 'subaru', 'honda']

print('ford' in autos)
print('audi' in autos)

for auto in autos:
    if auto == 'bmw':
        print(auto.upper())
    else:
        print(auto.title())

print(car == 'Subaru')
print(car == 'subaru')
print(car.lower() == 'subaru')
print(car.upper() == 'subaru')

if car != 'audi':
    print('I prefer Audi.')

