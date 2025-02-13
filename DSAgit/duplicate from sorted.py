
#Q.11 FIND THE DUPLICATES FROM SORTED ARRAY:
def duplicatefromsorted(arr,n):
    i=0
    for j in range(1,n):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
            
    return i+1
    

arr=[1,2,2,2,3]
n=len(arr)
print(duplicatefromsorted(arr,n))


