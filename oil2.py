sum = 0;
i = 0;
fib1 = 1;
fib2 = 2;
fib3 = 2;
while fib1 < 4000000:
	if fib1 % 2 == 0:
		sum += fib1;
	fib2 = fib1 + fib2;
	fib1 = fib3;
	fib3 = fib2;
	
print(sum)





