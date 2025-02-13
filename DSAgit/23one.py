N=int(input("enter N:"))
arr=list(map(int,input().split(" ")))
D=int(input("enter Date:"))
x=int(input("enter Fine:"))
count=0
if D%2==0:
 for i in arr:
    if i%2==0:
     count+=1
else:
    for i in arr:
      if i%2==0:
          count+=1

print(count*x)
        
    