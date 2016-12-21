import math

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
print(isprime(27))




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

print(findbigprime(600851475143))





