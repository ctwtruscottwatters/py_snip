#!/usr/bin/python3

def main():
    x = (1, 2, 3)
    print(type(x), x)
    x = [1, 2, 3]
    x.append(0)
    x.insert(0, 7)
    print(type(x), x)
    x = 'string'
    print(type(x), x, x[2:4])

if __name__ == "__main__": main()
