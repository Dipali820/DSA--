
#Q.7 AVERAGE OF ALL THE ELEMENTS IN THE ARRAY:
def avgofelements(arr,n):
  sum=0
  avg=0
  for i in range(len(arr)):
    sum+=arr[i]
  avg=sum//n
  return avg


arr=list(map(int,input("enter the array elements:").split()))
n=len(arr)
print(avgofelements(arr,n))