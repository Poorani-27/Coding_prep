'''

Factors of a Given Number

Problem Statement: Find all factors of a number or find all distinct divisors of a natural number.

Examples:

Example 1:
Input: n = 6
Output: 1,2,3,6
Explanation: 6 is divisible by 1,2,3,6

Example 2:
Input: n = 9
Output: 1,3,9
Explanation: 9 is divisible by 1,3,9'''

def finding_factors(num):
    factors=[]
    for i in range(1,num+1):
        if num%i == 0 :
            factors.append(i)
    return factors

num= int(input("enter a number : "))
result= finding_factors(num)
for i in result:
    print(i, end= " ")

'''
The time complexity of this code is O(n), where n is the value of the input number. This is because the loop runs from 1 to num.

The space complexity of this code is also O(n) because the `factors` list can potentially hold up to n elements, where n is the number of factors of the input number.

'''