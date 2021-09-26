#!/usr/bin/python

def isprime(n):
	if n == 1:
		return False
	for x in range(2, n):
		if n % x == 0:
			print("{} equals {} x {}".format(n, x, n // x))
			return False

	else:
		print(n, "is a prime number")
		return True

i = 0
while i < 1000:
	isprime(i)
	i = i + 1