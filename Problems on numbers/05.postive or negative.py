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
