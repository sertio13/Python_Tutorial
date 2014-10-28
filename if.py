__author__ = 'minda'

number = 23

guess = int(raw_input('Enter the number : '))

if guess ==number:

    #if block
    print('correct')
elif guess < number:
    print('higher')
else:
    print('lower')

print('done')


