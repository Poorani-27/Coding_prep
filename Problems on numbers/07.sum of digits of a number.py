'''

Sum Of Digits of A Number

Problem Statement: Given an integer, find the sum of digits of that integer.

Examples:

Example 1:
Input: N = 472
Output: 13
Explanation: The digits in the number are 4,7 and 2. Summing them up gives us a value of 13

Example 2:
Input: N = 102
Output: 3
Explanation: The digits in the number are 0, 1, and 2. Summing them up gives us a value of 3

'''
num=int(input())
num=str(num)
total=0
for i, n in enumerate(num):
    total +=int(n)

print(total)
