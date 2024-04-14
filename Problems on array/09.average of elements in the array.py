'''

Average of all the elements in the array


Problem Statement: Given an array, we have to find the average of all the elements in the array.

Examples:

Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: 3
Explanation: Average is the sum of all the elements divided by number of elements.Therefore (1+2+3+4+5)/5 = 3.

Example 2:
Input:  N=6, array[] = {1,2,1,1,5,1}
Output: 1.8
Explanation: Average is the sum of all the elements divided by number of elements.Therefore (1+2+1+1+5+1)/6 = 1.8

'''
arr= list(map(int,input().split()))
n=len(arr)
print("{:.2f}".format(sum(arr) / n))

'''
Time Complexity:

Calculating the sum of elements in the array using sum(arr) takes O(n) time, where n is the number of elements in the array.
Calculating the average by dividing the sum by the number of elements (sum(arr) / n) is a constant-time operation.
Therefore, the overall time complexity is O(n).
Space Complexity:

The space complexity is O(1) because the code only uses a fixed amount of additional space, regardless of the size of the input array. There are no additional data structures created or recursive function calls made that would scale with the input size.

'''