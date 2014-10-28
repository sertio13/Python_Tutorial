def print_max(a,b):

    if a > b:
        print a, 'is maximum'
    elif a == b:
        print a,'is equal to' ,b
    else:
        print b,'is maximum'


print_max(2,3)

x = 2
y = 31

print_max(x,y)

c = int(raw_input('enter number'))
d = int(raw_input('enter 2nd number'))

print_max(c,d)
