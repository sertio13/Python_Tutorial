__author__ = 'minda'

while True:
    s = raw_input('enter something')
    if s == 'quit':
        break

    if len(s) < 3 :
        print('too small')
        continue
    print s
