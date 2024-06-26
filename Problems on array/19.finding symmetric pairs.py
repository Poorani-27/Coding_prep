'''"Find all Symmetric Pairs in the array of pairs"

Problem Statement: Given an array of pairs, find all the symmetric pairs in the array.

Examples:

Example 1:
Input: (1,2),(2,1),(3,4),(4,5),(5,4)
Output: (2,1) (5,4)
Explanation: Since (1,2) and (2,1) are symmetric pairs and (4,5) and (5,4) are symmetric pairs.

Example 2:
Input: (1,5),(2,3),(4,2),(5,1),(2,4)
Output: (2,4) (5,1)
Explanation: Since (1,5) and (2,4) are symmetric pairs and (5,1) and (4,2) are symmetric pairs.
'''

def symmetric_pairs(arr):
    # new_arr = {}
    symmetric_pair =[]
    for pair in arr :
        first,second =pair
        if (second,first) in arr :
            if (first,second) not in symmetric_pair:
                symmetric_pair.append((second,first))
    print(symmetric_pair)

arr=[(1,5),(2,3),(4,2),(5,1),(2,4)]
symmetric_pairs(arr)
