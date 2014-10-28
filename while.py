__author__ = 'minda'

number = 23
running = True

while running:
    guess = int(raw_input('Enter the number : '))

    if guess ==number:

    #if block
        print('correct')
        running = False
    elif guess < number:
     print('higher')
    else:
        print('lower')

print('done')


