import math
def checkperfect(n):
    if n!=0:
      no=math.sqrt(n)
      square=no*no
      if square==n:
        return "yes it is perferct sqaure"
      else:
          return "no"
      
n=int(input("enter the number:"))
print(checkperfect(n))
        