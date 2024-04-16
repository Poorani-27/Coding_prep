'''

Find all the non-repeating elements in an array



Problem Statement: Find all the non-repeating elements for a given array. Outputs can be in any order.

Examples:

Example 1:
Input:
 Nums = [1,2,-1,1,3,1]
Output:
 2,-1,3
Explanation:
 1 is the only element in the given array which occurs thrice in the array. -1,2,3 occurs only once and hence, these are non-repeating elements of the given array.

Example 2:
Input:
 Nums = [1,2,3]
Output:
 1,2,3
Explanation:
 All elements present in the array occur once. Hence, every element is non-repeating.

'''






def finding_repeating(arr,n):
    frequency ={}
    repeating_elemnts =[]
    for num in arr :
        if num in frequency:
            frequency[num] +=1

        else :
            frequency[num] = 1
    for key,value in frequency.items() :
        if value == 1 :
            repeating_elemnts.append(key)
    print(repeating_elemnts)


arr=[1,2,-1,1,3,1]
n=len(arr)
finding_repeating(arr,n)
