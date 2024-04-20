'''

Problem Statement: Check if the given year is a leap year or not.

Examples:

Example 1:
Input: 1996
Output: Yes
Explanation: Since 1996 is a leap year answer is “Yes”.

Example 2:
Input: 2000
Output: Yes

Explanation: Since 2000 is a leap year answer is “Yes”

'''
year=int(input())
if ((year % 4 == 0) & (year % 100 != 0)) |(year % 400 == 0) : 
    print("Yes")
else:
     print('no')

'''

The time complexity of this code is O(1) because the execution time does not depend on the size of the input. 

The space complexity is also O(1) because the code only uses a constant amount of memory regardless of the size of the input.
'''
