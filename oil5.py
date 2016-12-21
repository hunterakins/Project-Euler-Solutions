
from __future__ import division
import math
import oil4


def numoccur(n,p):
	i = 0
	curr = p
	while n % curr == 0:
		i += 1
		curr = p*curr
	return i


print(numoccur(16,2))

print(numoccur(19,3))

print(numoccur(7, 2)) 

def smallest(n):
	i  = 2
	final = 2
	while i  < n:
		if final % i == 0:
			i += 1
		else:
			if oil4.isprime(i):
				final = final*i
			else:
				j = 2
				while j < i:
					exp = numoccur(i, j)
					while final % j**exp != 0:
						final = final*j
					else:	
						j = oil4.nextprime(j)
				i += 1
	return final


print(smallest(20))

