'''
Greatest of two numbers

Problem Statement: Given two numbers. Find the greatest of two numbers.

Examples:

Example 1:
Input: 1 3
Output: 3
Explanation: Answer is 3,since 3 is greater than 1.

Input: 1.123  1.124
Output: 1.124
Explanation: Answer is 1.124,since 1.124 is greater than 1.123.
'''



def max_num (a,b):
    result =max(a,b)
    return result

a,b=map(int,input().split())
print(max_num(a,b))