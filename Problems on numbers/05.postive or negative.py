'''

Check whether a number is positive or negative

Problem statement: Given a number n check whether it's positive or negative.

Examples:

Example 1:
Input: n=5
Output: Positive

Example2:
Input: n=-6
Output: Negative

'''

def pos_neg(num):
    if num>0 :
        print('positive')
    elif num == 0 :
        print("0 is neither pos nor neg")
    else:
        print("negative")

num=float(input())
pos_neg(num)

def check_sign(num):
    # Right shift the number by its bit length - 1
    # If the result is 0, the number is positive; if it's -1, the number is negative
    sign_bit = (num >> (num.bit_length() - 1)) & 1
    if sign_bit == 0:
        print("Positive")
    else:
        print("Negative")

# Example usage
num = int(input("Enter a number: "))
check_sign(num)