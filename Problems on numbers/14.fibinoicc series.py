'''
Print Fibonacci Series up to Nth term

Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.

Examples:

Example 1:
Input: N = 5
Output: 0 1 1 2 3 5
Explanation: 0 1 1 2 3 5 is the fibonacci series up to 5th term.(0 based indexing)

Example 2:
Input: 6

Output: 0 1 1 2 3 5 8
Explanation: 0 1 1 2 3 5 8 is the fibonacci series upto 6th term.(o based indexing)

'''
def fib(num):
    a,b =0,1
    fib_series=[]
    for i in range(num+1):
        fib_series.append(a)
        a,b=b,a+b
    for i in fib_series:
        print(i , end=" ")


num=int(input("number : "))

fib(num)