'''
Find LCM of two numbers

Problem Statement: Find lcm of two numbers.

Examples:

Example 1:
Input: num1 = 4,num2 = 8
Output: 8


Example 2:
Input: num1 = 3,num2 = 6
Output: 6


'''

def lcm(num1,num2):
    factors_num1=[]
    factors_num2=[]
    for i in range(1,num1+1):
        if num1%i==0:
            factors_num1.append(i)
    for i in range(1,num2+1):
        if num2%i==0:
            factors_num2.append(i)
    result = list(set(factors_num1) | set(factors_num2))
    print(result)
    print('lcm : ' , max(result))
     

    
num1, num2 =map(int,input("enter two numbers : ").split())

lcm(num1,num2)
