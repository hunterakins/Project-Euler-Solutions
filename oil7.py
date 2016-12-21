from __future__ import division
import oil4


def primenumber(n):
	init = 2
	i = 1
	while i < n:
		init = oil4.nextprime(init)
		i += 1
	return init
print(primenumber(1))

print(primenumber(6))

print(primenumber(10001))


