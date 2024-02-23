a = int(input("Enter a "))
b= int(input("Enter b "))
print(a,b)
a,b=b,a
print( "swapped", a,b)
 # using temp variables
a=3
b=5
print("Value of a and b :",a,b)
temp = a
a = b
b= temp
print(a,b)