'''

Factorial of a Number 

Problem Statement: Given a number X,  print its factorial.

To obtain the factorial of a number, it has to be multiplied by all the whole numbers preceding it. More precisely X! = X*(X-1)*(X-2) … 1.

Note: X  is always a positive number. 

Examples:

Example 1:
Input: X = 5
Output: 120
Explanation: 5! = 5*4*3*2*1

Example 2:
Input: X = 3
Output: 6
Explanation: 3!=3*2*1


'''

# 1.Recursion 

def fac(num):
    if num ==1 or num==0:
        return 1
    else :
        return num *fac(num-1)


num=int(input("enter a number : "))
print(fac(num))

'''
The time complexity of this recursive approach to finding the factorial of a number is O(n) because it involves n recursive calls, where n is the value of the input number.

The space complexity of this code is also O(n) because the recursion stack can have at most n frames, where n is the value of the input number.

'''
#2.Iterative approach

def fac(num):
    result = 1
    for i in range(1,num+1):
        result *=i 
    return result

num=int(input("enter a number : "))
print(fac(num))
 
'''
 The time complexity of this code is O(n) because it involves iterating over the numbers from 1 to n.

The space complexity of this code is O(1) because it only uses a constant amount of extra space regardless of the input size
 
 '''