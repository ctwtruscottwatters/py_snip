#!/usr/bin/python

# From my Python lectures. Trying to get a bit more practical by transfering from C/C++ to Python even to compile to an .EXE PORTABLE EXECUTABLE FORMAT BINARY
# Eager to learn pywin32 API, really drill down desktop GUI development and the real ins and outs of the Python standard library
# as well as object orientation, polymorphism, inheritance, and tricky classful things about the Python language as de-facto for development
# As I delve more into C and C++ however, instead of going the GNU way, I'm most certainly trying to think up large scale projects
# When I read Stephen Hawking's 'Large Scale Structure of Spacetime' it changed my life.
# Code borrowed from a circa 2007 Python 3 Lecture
# In C would love to write instead of 100 lines 100 headers or 100 multiple-.c-linkages
# Very interested in writing code that spans multiple headers, uses ingenuity and fine-grained and tailored approaches to solving CS problems
# e.g. source code for the TCP/IP protocol suite, their protocols in RFCs or MSDNs, file-formats or assembly language
# e.g. device driver programming, DLL programming, compiler, memory based / processor exploit mitigation technologies
# e.g. kernel compilation, race conditions and use-after-frees, heap overflows instead of just stack overflows
# recently wrote up an x64 stack overflow for my own code, really do need to stick the null byte in, e.g. 00007FFFFFFFFFFF
# ASLR

def isprime(n):
	if n == 1:
		return False
	for x in range(2, n):
		if n % x == 0:
			print("{} equals {} x {}".format(n, x, n//x))
			return False
	else:
		print("{} is a prime number :-)".format(n))

tai = 0
while tai < 20000:
	isprime(tai)
	tai = tai + 1
