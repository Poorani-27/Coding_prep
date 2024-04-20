'''Find GCD of two numbers

Problem Statement: Find the gcd of two numbers.

Examples
Example 1:
Input:
 num1 = 4, num2 = 8
Output:
 4
Explanation:
 Since 4 is the greatest number which divides both num1 and num2.

Example 2:
Input:
 num1 = 3, num2 = 6
Output:
 3
Explanation:
 Since 3 is the greatest number which divides both num1 and num2.'''



def gcd(num1,num2):
    factors_num1=[]
    factors_num2=[]
    for i in range(1,num1+1):
        if num1%i==0:
            factors_num1.append(i)
    for i in range(1,num2+1):
        if num2%i==0:
            factors_num2.append(i)
    result = list(set(factors_num1) & set(factors_num2))
    print(result)
    print('Gcd : ' , max(result))
     

    
num1, num2 =map(int,input("enter two numbers : ").split())

gcd(num1,num2)


'''

The time complexity of this code is O(n1 + n2), where n1 is the number of factors of num1 and n2 is the number of factors of num2.

The space complexity of this code is also O(n1 + n2) because we are storing the factors of num1 and num2 in separate list

'''
def gcd(num1,num2):
    while num2 :
        num1 , num2 = num2, num1%num2
    print('Gcd : ' , num1)
     

    
num1, num2 =map(int,input("enter two numbers : ").split())

gcd(num1,num2)


'''
In terms of time complexity, this code has a time complexity of O(log(min(num1, num2))) because it uses the Euclidean algorithm for finding the greatest common divisor (GCD). The number of iterations required for the algorithm is proportional to the number of digits in the smaller number.

The space complexity is O(1) because the code only uses a constant amount of extra space regardless of the input size.

'''