command = ''
started =False
while True:
    command = input('enter the commane: ').lower()
    if command=='start':
        if started:
            print('car is already started!!')
        else:
            started= True
            print('car started....')
    elif command =='stop':
        if not started:
            print('car is already stoped!')
        else:
            started=False
            print('car stoped!....')
    elif command=='quit':
        break
    else:
        print('sorry you press wrong command!!')

