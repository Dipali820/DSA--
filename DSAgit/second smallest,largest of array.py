	
#Q.2 FIND THE SECOND LARGEST AND SMALLEST ELEMENT IN AN ARRAY,
def secondlarsmall(a):
  a=sorted(set(a))
  if len(a)==1:
    return a[0]
  #for i in range(len(a)):
  smallest_second= a[1]
  largest_second=a[-2]
  return smallest_second,largest_second

a=[1,2,4,7,7,5]
n=len(a)
smallest_second,largest_second=secondlarsmall(a)
print("second smallest:",smallest_second)
print("second largest:",largest_second)




