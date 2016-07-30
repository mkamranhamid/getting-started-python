print('FIle is working')
cars = ['bmw','audii','ferrari','lamborghini']
#if else if and else withinh loop
for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car == 'audi':
        print(car.capitalize())
    else:
        print(car.title())

#if else
age1 = 10
age2 = 19
if (age1 > 9) and (age2 > 18):
    print('allowed')
else:
    print('not allowed')

#finds an item in array
if 'bmw' in cars:
    print('BMW Found')
if 'suzuki' not in cars:
    print('suzuki not Found')

if age1>=50:
    print('retired')
elif age1>=30:
    print('young')
elif age1>=18:
    print('cool')
else:
    print('not allowed to work')

plate = []
if plate:
    print('my plate full')
else:
    print('my plate is empty')
