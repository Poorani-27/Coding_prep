'''

Search an Element in an Array : Program CPP Java


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
def search(arr,k,n):
    for num in arr :
        if k==num :
            print("found at index",arr.index(k))
            return
    print('not found')
        
arr = [1,2,3,4,5]
n=len(arr)
k=9
search(arr,k,n)