'''

Find Median of the given Array

Problem Statement: Given an unsorted array, find the median of the given array.

Examples:

Example 1:
Input: [2,4,1,3,5]
Output: 3

Example 2:
Input: [2,5,1,7]
Output: 3.5

What is a Median?
Median is defined as the value which is present in the middle for a series of values. Note, in order to find the median of an array of integers, we must make sure they are sorted.

'''
arr = [2,5,1,7]
arr.sort()
n= len(arr)
if n %2 == 0 :
    median= (arr[n//2] + arr[n//2 -1]) /2
else :
    median = arr[n//2]
print(median)

'''

Time Complexity:

Sorting the array arr using the sort() method takes O(n log n) time, where n is the number of elements in the array. Sorting dominates the time complexity.
Finding the median involves constant-time operations such as accessing elements by index and performing arithmetic operations.
Therefore, the overall time complexity is O(n log n).
Space Complexity:

The space complexity is O(n) due to the space required to store the array arr.
Other variables like n and median require constant space, which does not depend on the size of the input array.
Therefore, the overall space complexity is O(n).

'''