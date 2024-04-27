'''

Problem Statement: Find the sum of numbers in the given range.

Examples:

Example 1:
Input: l=2, r=7
Output: 27
Explanation: 2+3+4+5+6+7=27. Therefore 27 is the answer.

Example 2:
Input: l=5, r=9
Output: 35
Explanation: 5+6+7+8+9=35. Therefore 35 is the answer.

'''

a, r = map(int,input().split())
result=[]
for i in range (a,r+1):
    result.append(i)
print(sum(result))

'''
Let's analyze the time and space complexity of the provided code:

### Time Complexity:
- The time complexity of the code depends on the number of iterations in the loop.
- The loop iterates from `a` to `r`, inclusive. So, the number of iterations is `r - a + 1`.
- Therefore, the time complexity of the loop is O(r - a).
- The `sum()` function also iterates through the elements of the `result` list once to calculate the sum. Since there are `r - a + 1` elements in the list, the time complexity of the `sum()` function is also O(r - a).
- Combining both, the overall time complexity of the code is O(r - a).

### Space Complexity:
- The space complexity of the code depends on the size of the `result` list.
- The `result` list stores all integers from `a` to `r`, inclusive. So, its size is `r - a + 1`.
- Therefore, the space complexity of the `result` list is O(r - a + 1).
- Additionally, there are a few variables (`a`, `r`, `i`, `result`) that occupy constant space regardless of the input size.
- Combining both, the overall space complexity of the code is O(r - a + 1).

In conclusion, the time complexity of the provided code is O(r - a), and the space complexity is also O(r - a + 1).

'''