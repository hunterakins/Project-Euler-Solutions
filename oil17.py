from __future__ import division
import math
import numpy as np 
import mymeth as mm 


# one, two, six  and ten have 3
# four, five and nine have 4
# three, seven and eight have 5
# eleven


one = 'one'
two = 'two'
three = 'three'
four = 'four'
five = 'five'
six = 'six'
seven  = 'seven'
eight = 'eight'
nine = 'nine'
ten = 'ten'
eleven = 'eleven'
twelve = 'twelve'
thirteen = 'thirteen'
fourteen = 'fourteen'
fifteen = 'fifteen'
sixteen = 'sixteen'
seventeen = 'seventeen'
eighteen = 'eighteen'
nineteen = 'nineteen'
twenty = 'twenty'
thirty = 'thirty'
forty = 'forty'
fifty = 'fifty'
sixty = 'sixty'
seventy = 'seventy'
eighty = 'eighty'
ninety = 'ninety'
hundred = 'hundred'
thousand = 'thousand'


numdict = {1:one,
2:two,
3:three ,
4:four ,
5:five ,
6:six,
7:seven  ,
8:eight ,
9:nine ,
10:ten,
11:eleven ,
12:twelve ,
13:thirteen ,
14:fourteen ,
15:fifteen ,
16:sixteen ,
17:seventeen ,
18:eighteen ,
19:nineteen ,
20:twenty ,
30:thirty ,
40:forty,
50:fifty,
60:sixty,
70:seventy ,
80:eighty ,
90:ninety ,
100:hundred ,
1000:thousand}																		

# convert positive integer to list format, then to string format
def listnum2txtstring(n):
	num = mm.inttolist(n)
	if n == 0:
		return ''
	elif len(num) == 1:
		return numdict[n]
	elif len(num) == 2 and num[0] == 1:
		return numdict[n]
	elif len(num) == 2 and num[1] == 0:
		return numdict[n]
	elif len(num) == 2:
		tens = num[0]
		ones = num[1]
		return numdict[tens*10]+numdict[ones]
	elif len(num) == 3 and num[1] == 0 and num[2] == 0:
		return numdict[num[0]] + 'hundred'
	elif len(num) == 3:
		hundreds = num[0]
		leftover = mm.listtonum(num[1:])
		return numdict[hundreds] + 'hundredand' + listnum2txtstring(leftover)
	else:
		return 'one' + 'thousand'

print(listnum2txtstring(20))



print(sum(map(len, (map(listnum2txtstring, range(1,1001))))))

