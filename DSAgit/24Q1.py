
def prime(n):
    if n>1:
        for i in range(2,n):
           if (n % i)==0:
              print(n,"is not prime")
              
        else:
               print(n,"is a prime number")
    
num=int(input("enter the num:"))
if (num>0):
    prime(num)
else:
    print("enter positive number:")
    