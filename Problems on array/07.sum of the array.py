'''
Calculate Sum of the Elements of the Array
Problem Statement: Given an array, we have to find the sum of all the elements in the array.

Examples:

Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: 15
Explanation: Sum of all the elements is 1+2+3+4+5 = 15

Example 2:
Input:  N=6, array[] = {1,2,1,1,5,1}
Output: 11
Explanation: Sum of all the elements is 1+2+1+1+5+1 = 11


'''
arr=[1,2,3,4,5]
print(sum(arr))

'''

Time Complexity:

The sum() function iterates over each element in the list once to calculate the sum. Therefore, the time complexity of the sum() function is O(n), where n is the number of elements in the list.
Since there are no other significant operations in the code, the overall time complexity is O(n).
Space Complexity:

The space complexity is O(1) because the code only uses a fixed amount of additional space, regardless of the size of the input list. This fixed amount of space includes the space required for the list arr and any additional variables created during execution, which do not depend on the size of the input list.

'''

def sum_of_array(arr,n):
    result = 0
    for i in range(n):
        
        result +=arr[i]
    print(result)

n=len(arr)
sum_of_array(arr,n)

'''

Time Complexity:

The time complexity of this function is O(n), where n is the number of elements in the array. This is because the function iterates through each element of the array once to calculate the sum.

Space Complexity:

The space complexity is O(1) because the function only uses a fixed amount of additional space, regardless of the size of the input array. In this case, the only additional variable used is result, which is an integer variable that stores the sum. Therefore, the space complexity does not depend on the size of the input array.

'''