#Q.5 CALCULATE THE SUM OF ARRAY ELEMENTS:

def sumofarrelements(arr):
  sum = 0
  for i in range(len(arr)):
    sum += arr[i]
  return sum

arr = list(map(int, input("Enter the elements separated by space: ").split()))
print(sumofarrelements(arr))