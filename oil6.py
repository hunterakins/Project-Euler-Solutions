
a = range(1,101)
square =  lambda x: x*x

squares = map(square, a)

summer = lambda x,y : x+y
sumsquares = reduce(summer, squares)

ready = reduce(summer, a)
result = square(ready) - sumsquares
print(result)

