'''

Calculate the Area of the Circle

Problem Statement: Given the radius of the circle, calculate the area of the circle.

Examples:

Example 1:
Input: N = 5
Output: 78.5
Explanation: Using formula  πr2 for finding area of circle we get area as 78.5

Example 2:
Input: N = 4
Output: 50.2
Explanation: Using formula  πr2 for finding area of circle we get area as 50.2


'''
def area_of_circle(r):
    print(3.14*r**2)

r=int(input("Radius : "))
area_of_circle(r)