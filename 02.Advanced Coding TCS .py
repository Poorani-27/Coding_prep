'''
 Given a maximum of hundred digit numbers  
 find the difference between the sum of the odd and the even positive digits. 
 Test cases 
 input 4567 
 expected outcome 2
   explanation : odd positions are 4 and 6 as the part of their position 1 and position 3 Both have sum 10. 
   Similarly, 5 and seven are at the position of 2 and 4 with the sum 12. 
   The difference between 12 - 10 equal to two.


'''

def odd_even(num):
    odd=[]
    even=[]
    for index, i in enumerate(num):
        if index %2==0 :
            even.append(index)
        else :
            odd.append(index)
    print(abs(sum(odd)-sum(even)))


num=4567
num=str(num)
odd_even(num)