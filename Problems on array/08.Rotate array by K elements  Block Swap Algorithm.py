'''

Rotate array by K elements : Block Swap Algorithm

Problem Statement: Given an array of n size, rotate the array by k elements using the Block Swap Algorithm.

Examples:

Example 1:
Input: N = 5, array[] = {1,2,3,4,5} K=2
Output: {3,4,5,1,2}
Explanation: Rotate the array to right by 2 elements.

Example 2:
Input: N = 7, array[] = {1,2,3,4,5,6,7} K=3
Output: {4,5,6,7,1,2,3}
Explanation: Rotate the array to right by 3 elements.


block swap algorithm

Divide the given array into two subarrays A and B where A stores the first ‘k’ elements and
B store next ‘n-k’ elements. If the size of both subarrays is not equal then perform block swap b/w A and B, where the block size is the size of smaller subarray and then reduce the size of subarray by block size. Repeat this until the size of both subarrays become equal. 

'''