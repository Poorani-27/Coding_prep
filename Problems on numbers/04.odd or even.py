'''Check whether a given number is even or odd

Problem Statement: Given a number n, check whether a given number is even or odd.

Examples:

Example 1:
Input: n=5
Output: odd
Explanation: 5 is not divisible by 2.
 
Example 2:  
Input: n=6
Output: even
Explanation: 6 is divisible by 2.'''

def odd_even (num):

    if num %2  == 0 :
        print("even")
    else:
        print("odd")

num=float(input('num = '))
odd_even(num)