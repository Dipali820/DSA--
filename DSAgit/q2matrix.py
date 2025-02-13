R=int(input("enter R:"))
C=int(input("enter c:"))
matrix=[]
for i in range(R):
    temp=[]
    for j in range (C):
        x=int(input())
        temp.append(x)
    matrix.append(temp)
    
prev_cnt=0
ans=0
#trversing 
for i in  range (R):
    curr_count=matrix[i].count(1)
    if curr_count>prev_cnt:
        prev_cnt=curr_count
        ans=i+1
print(ans)
    