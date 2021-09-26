#!/usr/bin/python3

def main():
    func(1)
    func(2)
    func(7)

def func(a = 5):
    for i in range(a, 10):
        print(i, end='')
    print()

if __name__ == "__main__": main()