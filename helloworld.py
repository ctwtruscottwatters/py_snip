#!/usr/bin/python

print("Hello, World!")

a, b = 1, 0

if a < b:
	print('a ({}) is less than b ({})'.format(a, b))
else:
	print('a ({}) is not less than b ({})'.format(a, b))

i, j, k = 0, 1, 1

while j < 50:
	print(j)
	i, j = j, i + j

file_handle = open('scratchpad.cpp')
for line in file_handle.readlines():
	print(line, end='')