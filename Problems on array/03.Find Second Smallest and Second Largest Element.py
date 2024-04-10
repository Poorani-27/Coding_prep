'''Find Second Smallest and Second Largest Element in an array
Problem Statement: Given an array, find the second smallest and second largest element in the array.
Print ‘-1’ in the event that either of them doesn’t exist.
Input:
 [1,2,4,7,7,5]
Output:
 Second Smallest : 2
	Second Largest : 5
Explanation:
 The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

Example 2:
Input:
 [1]
Output:
 Second Smallest : -1
	Second Largest : -1
Explanation:
 Since there is only one element in the array, it is the largest and smallest element present in the array. There is no second largest or second smallest element present.
'''

def solution_1 (arr):
    arr=set(sorted(arr))
    print(arr)
    arr=list(arr)
    if len(arr) >2 :
        print(f"second smallest element {arr[1]}\n second largest element {arr[-2]}")
    elif len(arr) ==2 :
          print(f"second smallest element {arr[0]}\n second largest element {arr[1]}")
    else:
        print("-1")

def solution_2(arr, n):
    if n == 0 or n == 1:
        print(-1, -1)  # edge case when only one element is present in array
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    print("Second smallest is", second_small)
    print("Second largest is", second_large)

     



arr= list(map(int,input().split()))
n=len(arr)
solution_1(arr)
solution_2(arr,n)






solution = '''

1. Brute Force Approach : sorting and finding (only if there is no duplicates in the array) or converting the array to set to remove duplicates and then sorting and finding
Time complexity :O(n log n)
Space complexity : O(n)

2.










'''