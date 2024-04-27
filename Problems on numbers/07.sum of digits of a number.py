'''

Sum Of Digits of A Number

Problem Statement: Given an integer, find the sum of digits of that integer.

Examples:

Example 1:
Input: N = 472
Output: 13
Explanation: The digits in the number are 4,7 and 2. Summing them up gives us a value of 13

Example 2:
Input: N = 102
Output: 3
Explanation: The digits in the number are 0, 1, and 2. Summing them up gives us a value of 3

'''
num=int(input())
num=str(num)
total=0
for i, n in enumerate(num):
    total +=int(n)

print(total)

'''
Let's analyze the time and space complexity of the provided code:

### Time Complexity:
- The time complexity of the code depends on the number of digits in the input number `num`.
- Converting the input number to a string takes O(log(num)) time complexity.
- The loop iterates over each digit of the string representation of the input number, so its time complexity is O(digits), where `digits` is the number of digits in the input number.
- Inside the loop, each digit is converted to an integer using `int(n)`, which has constant time complexity.
- Therefore, the overall time complexity of the code is O(log(num) + digits).

### Space Complexity:
- The space complexity of the code depends on the size of the input number `num`, as well as the size of the variables used in the code.
- Converting the input number to a string creates a new string with the same number of characters as the input number, so its space complexity is O(log(num)).
- The `total` variable occupies constant space, and the loop variables (`i` and `n`) also occupy constant space.
- Therefore, the overall space complexity of the code is O(log(num)), as the dominant factor is the size of the input number.

In conclusion, the time complexity of the provided code is O(log(num) + digits), and the space complexity is O(log(num)), where `num` is the input number and `digits` is the number of digits in the input number.

'''