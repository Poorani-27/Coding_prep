# Adding two numbers
''' Using “+” operator
Defining a function that adds two number
Using operator.add method
Using lambda function
Using Recursive function'''
#+operator
a=2
b=3
print(a+b)
#function
def add(a,b):
    return a+b
a=12
b=32
sum=add(a,b)
print(sum)
#using operator.add method
import operator
a=11
b=22
sum = operator.add(a,b)
print(sum)
#lambda
a=123
b=123
sum = lambda x, y: x + y
print(sum(a,b))
#recursion
# Define a recursive function to add two numbers
def add(x, y):
	if y == 0:
		return x
	else:
		return add(x + 1, y - 1)
result = add(22,44)
print(result)