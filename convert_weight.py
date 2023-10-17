weight = int(input('enter your weight: '))
unit = input('press l in punds or k for in kg: ')
if unit.lower()=='l':
    converted = weight*.45
    print (f'you are {converted} kg!')
elif unit.lower()=='k':
    converted = weight/.45
    print(f'you are {converted} pounds')
else:
    print('plese press right key!!')