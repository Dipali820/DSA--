N=int(input("enter N:"))
arr=[]
for i in range(N):
    arr.append(input())
    
    
shoe_dict={}
for i in arr:
    size=i[0]
    side=i[-1]
    if size not in shoe_dict:
        shoe_dict={'L'==0,'R'== 0}
    shoe_dict
    [side]+=1
    
ans=0
for size in shoe_dict:
    ans+=min(shoe_dict[size]['L'],shoe_dict[size]['R'])
print(ans)        

