''' 

def reversing_array(arr):
    for num in reversed(arr):
        print(num,end=" ")

arr = list(map(int, input().split()))
reversing_array(arr)


 '''
#the time complexity is O(n), and the space complexity is O(1), where n is the number of elements in the input array.

def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")
    print()
def revrse(arr, start, end ):
    if start < end :
        arr[start], arr[end] = arr[end], arr[start]
        revrse(arr,start +1, end-1)
    
arr= [1,2,3,4,5,6]
n= len(arr)
revrse(arr, 0, n-1)
printArray(arr,n)

#the time complexity is O(n), and the space complexity is O(n), where n is the number of elements in the input array.


