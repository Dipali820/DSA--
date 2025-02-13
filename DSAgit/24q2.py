T=int(input("enter time:"))
E=[]
E=list(map(int,input().split(" ")))
L=[]
L=list(map(int,input().split(" ")))
r=0
guest=list()   

for i in range(T):
    r=r+E[i]-L[i]
    guest.append(r)
    
print(max(guest))

    