N=int(input("enter N:"))
B=list()
for i in range (N):
    B.append(input().lower())
    count=0
for i in B:
      if B.count(i)%2!=0:
          #count+=i
          print(i)
          break
      else:
        print("all are even")