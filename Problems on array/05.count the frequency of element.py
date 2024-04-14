def frequency_count(arr,n):
    mp={}
    for i in range(n):
        if arr[i] in mp :
            mp[arr[i]] += 1
        else :
            mp[arr[i]] =1
    for x in mp :
        print(x,mp[x])
arr=[1,1,3,3,2,2,3,3,3,4,4,4,4,4,5,5,5,5,5]
n=len(arr)
frequency_count(arr,n)

#time complexity O(n) and space complexity O(n)