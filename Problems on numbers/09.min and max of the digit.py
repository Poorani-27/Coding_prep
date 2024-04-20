'''

Maximum and Minimum Digit in a Number

Problem Statement: Given a number N, print the smallest and largest digits present in the number.
Example 1:
Input: N = 2746
Output: Largest digit: 7
        Smallest digit: 2
Explanation: By simply going through the digits of 
the number, we figure out the largest and smallest 
digit in the number.

Example 2:
Input: N = 23004
Output: Largest digit : 4
        Smallest digit : 0
Explanation: By simply going through the digits of 
the number, we figure out the largest and smallest 
digit in the number.
'''



def min_max(num):
    num=str(num)
    result=[]
    for i,digit in enumerate(num):
        result.append(int(digit))

    print("Largest : ",max(result))
    print("Smallest : ",min(result))
        

number = input(("Enter the number : "))
min_max(number)

'''
The time complexity of this code is O(n), where n is the number of digits in the input number.

The space complexity of this code is also O(n) because the `result` list will contain the same number of elements as the number of digits in the input number.

'''