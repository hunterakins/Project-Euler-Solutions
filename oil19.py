from __future__ import division
import mymeth as mm 

# This problem is to calculate the number of Sundays in the 20th century that occurred on the 1st of the month.  The century starts on 1 Jan 1901 and ends on Dec 31 2000. Leap years occur every 4th year. 
# This seems like an object oriented programming kind of problem. No matter. 
# I need a condition, "leap year", which is true if the year is divisible by 4. Okay so that's easy. 



catalog = [31,29,31,30,31,30,31,31,30,31,30,31]		#number of days in each month in a normal year
for i in range(1,12):
	catalog[i] = catalog[i] + catalog[i-1]

# now catalog[i] gives the number of days leading up to and containing the ith month. 
# i.e. catalog[1] gives the number x such that if the day of the year is less than x, the day is before or in the ith month
# THE STRATEGY: increment the days by one until the year becomes 2001. If the day mod 7 == 0, 


def answer():
	year = 1901
	specialsundays = 0
	clock = 2
	while year < 2001:  
		days = 365
		if year % 4 == 0:
			for i in range(1,12):
				catalog[i] = catalog[i] + 1	
			days = 366
		if (year - 1) % 4 == 0:
			for i in range(1, 12):
				catalog[i] = catalog[i] - 1
		month = 0
		monthdays = catalog[month]	
		curr = 1                         # keeps track of the days in the year                 
		if clock % 7 == 0:
			specialsundays += 1
		while curr < days:
			curr += 1
			clock += 1
			if not curr <= monthdays:
				if clock % 7 == 0:
					specialsundays += 1
				month += 1
				if month < 12:
					monthdays = catalog[month]
		year += 1
	return specialsundays


print(answer())

