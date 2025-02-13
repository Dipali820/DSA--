N=int(input("enter N:"))
arr=list(map(int,input().split(" ")))
ans=0
curr_sum=0
start=0
for end in range(N):
    curr_sum+=arr[end]
    while curr_sum>= K:
        curr_sum-=arr[start]
        start+=1 
    ans=max(ans,end-start+1)
    
print(ans)