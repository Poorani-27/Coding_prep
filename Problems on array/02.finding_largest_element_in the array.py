'''
Problem Statement: Given an array, we have to find the largest element in the array

Example 1:
Input:
 arr[] = {2,5,1,3,0};
Output:
 5
Explanation:
 5 is the largest element in the array. 

Example2:
Input:
 arr[] = {8,10,5,7,9};
Output:
 10
Explanation:
 10 is the largest element in the array. 

'''
def finding_largest_element(arr):
    arr.sort()
    print("largest number : " ,arr[-1])
def max_elemnt(arr):
    print("max : ",max(arr))
arr = list(map(int,input("\nEnter elements : ").split()))
finding_largest_element(arr)
max_elemnt(arr)
solution_1 = '''1.sort the array and find the element at -1 index (last element)
Time complexity = O(n log n)
space complexity = O(1)'''
solution_2 = '''\n\n2.using max 
time complexity = O(n)
space complexity = O(1)'''
print("\n",solution_1,solution_2)