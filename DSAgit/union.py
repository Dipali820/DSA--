a=[1,2,3,4,5]
b=[1,2,3]   
    #Function to return the count of number of elements in union of two arrays.
def findUnion(self, a, b):
        count=0
        for i in range(a):
          #for j in range(b):
               if a[i] in b:
                   au=count+1
               else:
                   bu=count+1
        return au+bu
  