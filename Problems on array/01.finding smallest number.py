'''
problem statement : You Are given With a array . you need to find the smallest element 
example : 
input arr[]={1.9,0,3,5,6}
output = 0

'''
solution_1 = '''sort and find the element at 0 th index
1. Time Complexity: O(n log n) due to sorting.
2. Space Complexity: O(n) due to the space required for storing the input array and the temporary space used during sorting.

'''
solution_2= '''using min
1.Time Complexity: O(n) due to the linear scan to find the minimum element.
2.Space Complexity: O(1) because no extra space is used.
'''
def find_smallest_element(arr):
    arr=sorted(arr)
    print("smallest element ",arr[0])

def min_element(arr):
    print("minimum value ",min(arr))

arr=list(map(int,input("\nEnter the elements separated by space : ").split()))
find_smallest_element(arr)
min_element(arr)
print("\n",solution_1,solution_2 )