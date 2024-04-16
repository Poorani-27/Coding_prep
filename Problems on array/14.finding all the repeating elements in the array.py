def finding_repeating(arr,n):
    frequency ={}
    repeating_elemnts =[]
    for num in arr :
        if num in frequency:
            frequency[num] +=1

        else :
            frequency[num] = 1
    for key,value in frequency.items() :
        if value >1 :
            repeating_elemnts.append(key)
    print(repeating_elemnts)


arr=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5]
n=len(arr)
finding_repeating(arr,n)
