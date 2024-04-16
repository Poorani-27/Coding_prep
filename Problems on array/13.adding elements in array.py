'''
Adding Element in an Array

Problem Statement: Given an array of N integers, write a program to add an array element at the beginning, end, and at a specific position.

Example:
Input: N = 5, array[] = {1,2,3,4,5}
insertbeginning(6)
insertending(7)
insertatpos(8,4)
Output: 6,1,2,8,3,4,5,7
Explanation: 6 is added at the beginning and 7 is added at the end and 8 is added at position 4 

'''

def adding_elements(arr,start,end,in_pos,n):
    arr.insert(0,start)
    arr.insert(n,in_pos)
    arr.append(end)
    print(arr)

arr=[1,2,3,4,5]
a=6
b=7
c=8
n=4
adding_elements(arr,a,b,c,n)