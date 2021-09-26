#!/usr/bin/python

def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def getprimes(prime = 1):
    while(True):
        if isprime(prime): yield prime
        prime = prime + 1

prime = 0
for prime in getprimes(prime):
    if prime > 1000: break
    print(prime)
    prime += 1
