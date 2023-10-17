for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
for i in range(5,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()
numbers= [5,2,5,2,2]
for x in numbers:
    print('*'*x)
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output+='X'
    print(output)
