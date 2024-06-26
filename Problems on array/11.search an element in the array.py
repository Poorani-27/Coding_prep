'''
earch an Element in an Array


Problem Statement: Search an element in an array and return its position

Examples:

Example 1:
Input: array[] = {1,2,3,4,5} k=3                                                                              
Output: 2                                                                                                         
Explanation: The answer is 2 because 3 is present at 2nd index.

Example 2:
Input: array[]={6,7,9,5,3,10} k=10
Output: 5
Explanation: The answer is 5 because 10 is present at 5th index.
'''

def finding_element(arr,k):
    if k in arr :
        print (arr.index(k))

arr=[1,2,3,4,5]
k=3
finding_element(arr,k)

'''Time Complexity: O(n)
Space Complexity: O(1)'''