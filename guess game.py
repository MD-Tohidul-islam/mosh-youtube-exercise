i=0
while i<3:
    win_number = 55
    guess = int(input('guess a number: '))
    if guess == win_number:
        print('you win!!!!')
        break
    elif guess < win_number:
        print('too low')
    else:
        print('too high')
    i+=1