
def median(arr):
    n=len(arr)
    arr.sort()
    if len(arr)%2==0:
        m1=arr[n//2]
        m2=arr[(n//2)-1]
        return(m1+m2)/2
    else:
        return arr[n//2]
        


N=int(input("enter N:"))
matrix=[]
for i in range(N):
    arr=list(map(int,input().split(" ")))
    matrix.append(arr)
    
ans=1000
for i in matrix:
    ans=min(ans,median(i))
print(ans)
