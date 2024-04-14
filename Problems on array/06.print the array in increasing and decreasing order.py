'''

Rearrange array in increasing-decreasing order


5

0
Problem Statement: Rearrange the array such that the first half is arranged in increasing order, and the second half is arranged in decreasing order

Examples:

Example 1:
Input: 8 7 1 6 5 9
Output: 1 5 6 9 8 7
Explanation: First three elements are in the ascending order and next three elements are in the descending order.

Example 2:
Input: 4 2 8 6 15 5 9 20
Output: 2 4 5 6 20 15 9 8


'''

def arranging_the_array(arr,n):
    arr.sort()
    arr_1=arr[:n//2]
    arr_2=arr[n//2:]
    arr_2=list(reversed(arr_2))
    result = arr_1 + arr_2
    print(result)

arr=[8,7,1,6,5,9]
n=len(arr)
arranging_the_array(arr,n)


'''

Time Complexity:

Sorting the array takes O(n log n) time.
Slicing the array to create arr_1 and arr_2 takes O(n) time.
Reversing arr_2 takes O(n) time.
Concatenating arr_1 and arr_2 takes O(n) time.
Overall, the time complexity is dominated by the sorting operation, so the time complexity is O(n log n).
Space Complexity:

The space complexity is O(n) because we create two additional arrays arr_1 and arr_2, each of size approximately n//2, and a list containing the reversed arr_2, which also has size approximately n//2. Thus, the total space complexity is proportional to the size of the input array, n.

'''