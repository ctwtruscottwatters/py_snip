#!/usr/bin/python3


def main():
    a, b = 0, 1
    if a <= b:
        print('a ({}) is less than or equal to b ({})'.format(a, b))
    elif a >= b:
     print('a ({}) is greater than or equal to b ({})'.format(a, b))
    else:
     print('other scenario')
     new()

def new():
     i = 1
     j = 2
     k = 3


     if ((int(i) == int(1)) and (int(j) == int(2))):
         print('a is equal to one and b is equal to 2')
     elif j == 3:
         print('elif')
     elif j == 2 or k == 3:
         print('elif')
     else:
         print('nothing at all')



if __name__ == "__main__": main()