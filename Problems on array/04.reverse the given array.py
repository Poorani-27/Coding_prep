def reversing_array(arr):
    for num in reversed(arr):
        print(num, end=" ")

arr = list(map(int, input().split()))
reversing_array(arr)
#the time complexity is O(n), and the space complexity is O(1), where n is the number of elements in the input array.