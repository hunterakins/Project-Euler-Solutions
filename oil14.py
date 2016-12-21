from __future__ import division
import math
import mymeth as mm 
import numpy as np 
import time
import matplotlib.pyplot as plt 



# calculates the next collatz number from n
def collatz(n):
	if n == 1:
		return 
	elif n % 2 == 0:
		return n / 2
	else: 
		return (3*n)+1

# generates a sequence of collatz number starting from n
def genseq(n):
	seq = [n]
	curr = collatz(n)
	seq.append(curr)
	while curr != 1:
		curr = collatz(curr)
		seq.append(curr)
	return seq

# calculate the length of the collatz sequence beginning with n
def seqcount(n):
	i = 1
	curr = collatz(n)
	while curr > n:
		curr = collatz(curr)
		i += 1
	return [i,curr] 


def maxcount(n):
	l = np.zeros((2,n))
	l[0,0] = 1
	l[1,0] = 1
	for i in range(2,n+1):
		curr = seqcount(i)
		l[0, i-1] = i
		l[1, i-1] = curr[0] + l[1,curr[1]-1]
	maxy = max(l[1,:])
	ind = np.argmax(l[1,:])
	return l
# if you want to get the answer to the pe problem, change the output of maxcount to ind

finalanswer = maxcount(100)



fig = plt.plot(finalanswer[0,:], finalanswer[1,:],'ro')
#ax = fig.add_subplot(111)
#ax.set_title('Collatz Sequence Length vs. Starting Value')
#ax.set_xlabel('Starting value')
#ax.set_ylabel('Length')
plt.show(fig)