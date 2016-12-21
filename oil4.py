import math
import time


def isprime(n):
	cond = True;
	i = 2;
	while i <= n**0.5:
		if n % i == 0:
			return False;
		else:
			i += 1;
	return cond;

def nextprime(n):
	if  n % 2 == 0:
		p = n + 1;
		while not isprime(p):
			p += 2;
		return p;
	else:
		p = n + 2;
		while not isprime(p):
			p += 2;	
		return p	





def findbigprime(n):
	prime = 2;
	curr = n;
	lim = n**0.5
	if isprime(n):
		return n
	else:
		while prime <= lim:
		 	if curr % prime == 0 and isprime(curr/prime):
		 		return curr/prime;
	 		elif curr % prime == 0:
	 			curr = curr/prime;
			else:
				prime = nextprime(prime);
		return curr


def inttolist(n):
	dig = n
	l = [];
	while dig != 0:
		l.insert(0,int(dig % 10))
		dig = (dig - dig %10) /10
	return l


def ispalindrome(n):
	item = inttolist(n)
	cond = True
	while len(item) >= 1:
		if item[0] == item[-1]:
			item = item[1:-1]
		else:
			return False
	return cond

def nextpalindrome(palin):
	l = len(palin)
	if l % 2 == 0:
		i = l/2 - 1
		if palin[i] != 0:
			palin[i] = palin[i]-1
			palin[i+1] = palin[i+1] - 1
			return palin
		while palin[i] == 0:
			i -= 1	
		palin[i] = palin[i] - 1
		palin[-i-1] = palin[-i-1] - 1
		palin[i+1] = 9
		palin[-i-2] = 9
		return palin
	else:
		i = math.floor(l/2)
		if palin[i] != 0:
			palin[i] = palin[i] - 1
		else:
			while palin[i] == 0:
				i -= 1
			palin[i] = palin[i] - 1
			palin[i+1] = 9
			palin[-i-2] = palin[-i-1] - 1
			paln[-i-2] = 9 
		return palin


def palindromelist(starter):
	curr = starter
	final = [curr]
	while curr[0] >= 1:
		curr = nextpalindrome(curr)
		final.append(curr[:])
	return final

def listtonum(numlist):
	l = len(numlist)
	i = 1
	num = 0
	while i <= len(numlist):
		num += numlist[-i]*10**(i-1)
		i += 1
	return num

def ndigit(n, dig):
	if len(inttolist(n)) == dig:
		return True
	else:
		return False

def prodofthreedig(n):  
	i = 100
	if isprime(n):
		return False
	else:
		while i <= n**0.5 and ndigit(i,3):
			if n % i == 0 and ndigit(n/i,3):
				return True
			i += 1
		return False


A = palindromelist([9,9,9,9,9,9])
A.pop()
A.pop(0)


def whatiwant():
	i = 0
	while not prodofthreedig(listtonum(A[i])):
		i += 1
	return listtonum(A[i])
print('And the answer to number 4 is....')
print(whatiwant())



def sievemoney(n): #calculates all the primes less than and including n
	primer = 2
	listy = [0]*n 
	while primer <= n:
		i = 2*primer
		while i < n:
			if listy[i] == 0:
				listy[i] = 1
			i += primer
		j = primer+1
		if j == n:
			return listy
		while listy[j] == 1:
			j += 1
			if j == n:
				return listy
		primer = j		
	return listy

A = sievemoney(2000000)

def sievetonum(sieve):
	n = len(sieve)
	i = 3
	nums = [2]
	while i < n:
		if sieve[i] == 0:
			nums.append(i)
		i += 2
	return nums

B = sievetonum(A)
whatiwant = sum(B)
print(whatiwant)

start_time = time.time()
sievemoney(2000000)
print("--- %s seconds ---" % (time.time() - start_time))