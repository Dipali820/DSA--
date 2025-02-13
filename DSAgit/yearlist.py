year=[2200,2350,2600,2130,2190]
print(year)
print("pxtra pay as compared to jan",year[1]-year[0])
sum=0
for i in range (len(year)):
    if i<3:
      sum=sum+year[i]
print("Total expense in first quarter",sum)
#3
if 2000 in list:
    print("yes")
    