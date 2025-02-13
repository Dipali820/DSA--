
#Q.8 FIND THE MEDIAN OF THE GIVEN ARRAY:
def medianofarray(arr,n):
  for i in range(len(arr)):
    if arr[i]%2==0:
      mid=arr[n//2]+arr[n//2-1]
    else:
      mid=arr[n//2]
  return mid
arr=[2,4,1,3,5,6]
n=len(arr)
print(medianofarray(arr,n))
