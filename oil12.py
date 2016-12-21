from __future__ import division
import math
import mymeth as mm
import time	

init = time.time()

isfact = lambda x,y: y % x == 0
primelist = mm.sievetonum(mm.sieve(100000000))

primetime = time.time()
print("primetime")
print(primetime - init)

# is fact takes in two arguments: tests if the first one divides the second



def primefactors(n):
# takes in a number n and finds its prime factors
		
	relfact = lambda x: isfact(x, n)
	if n <= 10000000:
		factors = primelist[0:n]
		factors = filter(relfact, factors)
		return factors
	else:
		sievelist = mm.sieve(n)
		factors = mm.sievetonum(sievelist)
		return factors


def primemult(n, factors):
	# takes in a number n and calculates the multiplicity of its prime factors. it returns the multiplicity of its primes in a list
	largo = len(factors)
	multlist = [-1]*largo
	for i in range(largo):
		prime = factors[i]
		curr = prime 
		count = 0
		while isfact(curr, n):
			count += 1
			multlist[i] += 1
			curr = prime**count
	return multlist

factors = primefactors(28)
multlist = primemult(28, factors)



add1 = lambda x: x + 1
prod = lambda x, y: x * y
def multprod(multlist):
	# takes in a list whose elements are the respective multiplicities of the primes in some number and outputs the product of the (multiplicities + 1)
	finlist = map(add1, multlist)
	return reduce(prod, finlist)



def divnumber(n):
	# takes in a number and calculates its total number of divisors
	factors = primefactors(n)
	multlist = primemult(n, factors)
	return multprod(multlist)


def trinumaug(n, ind, steps):
	# takes in a trinum n indexed by ind and number of steps "steps" and calculates the n+steps trinum
	starter = ind+1
	finalnum = n
	i = 0
	while i < steps:
		finalnum += starter
		starter += 1
		i+= 1
	return finalnum


def triangularnum(): 
	# finds the triangular number with 500 divisors
	curr = [6,3]
	divisors = 1
	while divisors < 200:
		curr[0] = trinumaug(curr[0], curr[1], 1)
		curr[1] += 1 
		# curr is the ith triangular numbe
		divisors = divnumber(curr[0])
	return curr

answer = triangularnum()
print(answer[0])
print(answer[1])

end = time.time()
print("tot time")
print(end - init)

A = range(73920)
print(sum(A))