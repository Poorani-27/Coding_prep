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
    a, b = 0, 1
    fib_series = []  # Space complexity: O(n)
    
    # Time complexity: O(n)
    for i in range(num + 1):
        fib_series.append(a)
        a, b = b, a + b
        
    # Printing the Fibonacci series
    for i in fib_series:
        print(i, end=" ")

num = int(input("Enter a number: "))
fib(num)
#------------------------------------------------------------------------------------------------------------------
def fib(num):
    a, b = 0, 1
    
    # Print the first two Fibonacci numbers
    print(a, end=" ")
    print(b, end=" ")
    
    for _ in range(2, num + 1):
        # Calculate the next Fibonacci number
        c = a + b
        print(c, end=" ")
        
        # Update the values of a and b for the next iteration
        a, b = b, c

num = int(input("Enter a number: "))
fib(num)

# Time Complexity: O(n) and  Space Complexity: O(1)