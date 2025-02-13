def avg(arr,n):
    sum=0
    for  i in range(n):
    
        sum += arr[i]
    return sum/n
    
        


arr=int(input("enter array elements:"))
print(type(arr))
n=len(str(arr))
print(avg(arr,n))