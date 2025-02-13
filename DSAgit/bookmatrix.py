N=int(input("enter N:"))
#dp=list(map(int,input().split(" ")))

dp=[0]*(N+1)
#THIS IS BEST CASE
dp[0]=1
dp[1]=0
for i in range(2,N+1):
    dp[i]=((i-1)*(dp[i-1]+dp[i-2]))

print(dp[N])

 