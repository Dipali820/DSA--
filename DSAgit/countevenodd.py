arr=[2,3,4,5,6]
evencount=0
oddcount=0
for i in range(len(arr)):
    if i%2==0:
        evencount+=1
    else:
        oddcount+=1
        
print([evencount,oddcount])
