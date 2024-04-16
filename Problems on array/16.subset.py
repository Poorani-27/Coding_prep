def subset(arr_1, arr_2):
    arr_1.sort()
    arr_2.sort()

    arr_1 = set(arr_1)
    arr_2 = set(arr_2)

    for num in arr_2:
        if num not in arr_1:
            print("No")
            return  # Exit the function if an element in arr_2 is not in arr_1
    
    print("Yes")  # If all elements in arr_2 are found in arr_1, print "Yes"

arr_1 = [1, 3, 4, 5, 2]
arr_2 = [4, 5,6,2]

subset(arr_1, arr_2)
