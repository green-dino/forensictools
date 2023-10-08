#understanding conditional loops

while True:
    x = float(input('value for x:'))
    y = float(input('value for y:'))
    z = float(input('value for z:'))

    if x == y:
        print('x is equal to y')
    elif x == z:
        print ('x equals z')
    else:
        print('try again')
    
    play_again = input('play again? (y/n):')
    if play_again.lower() != 'y':
        break