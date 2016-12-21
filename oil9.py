from __future__ import division

square = lambda x: x*x
squareslist = map(square,range(100))

squaretest = lambda x: (x**0.5*10) % 10 == 0


listsquaretest = lambda x: squaretest(x[0]) and squaretest(x[1]) and squaretest(x[2])


def sumtothous():
	candidates = []
	i = 0
	for a in range(3,997):
		i = 1
		while i < a-i < 1000:
			adder = [i, a-i, 1000-a]
			candidates.append(adder[:])
			i+=1
	return candidates


candidates = sumtothous()

pythagorean = lambda x: (x[0])**2 + (x[1])**2 == (x[2])**2

print(pythagorean([5,12,13]))

myprecious = filter(pythagorean, candidates)

print(myprecious)

mult = lambda x, y: x*y
print(myprecious[0])

print(reduce(mult, myprecious[0]))