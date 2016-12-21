from __future__ import division
import oil4 as mine
import time

listy = [2]

now = time.time()
A = mine.sievemoney(2000000)
B = mine.sievetonum(A)
that = sum(B)
print(that)
end = time.time()
print('begin...', now, 'and end', end)
