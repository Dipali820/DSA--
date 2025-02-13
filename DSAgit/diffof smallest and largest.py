
#Q. FIND DIFFERENCE BETWWEN SMALLEST AND LARGEST NUMBER.
a=[1,2,4,3,6]
a.sort() #[1,2,3,4,6]
new=[]
#for i in range len(a):
ans=a[1]-a[-1]
  #new.append(ans)
print(new)

#PRIME COADING CRASH ARRAY 
#Q.1 FIND THE MINNIMUM ELEMENT IN ARRAY
#METHOD 1:
def mini(a):
  a.sort()
  print(a[0])

a=[2,5,1,3,0]
mini(a)

#METHOD 2:
def formin(a):
  ans=float('inf')
  for i in range(len(a)):
    ans=min(ans,a[i])
  print(ans)

a=list(map(int,input("enter the elements seperated by spaces:").split()))
formin(a)