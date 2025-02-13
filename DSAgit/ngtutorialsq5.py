s1=list(input("enter first word:"))
s2=list(input("enter second word:"))
s3=input("enter third word:")

vowels=['a','e','i','o','u']
for i in range (len(s1)):
    if s1[i].lower() in vowels:
        s1[i]='*'
    
for i in range(len(s2)):
    if s2[i].lower()!= vowels:
        s2[i]='@'
        
result=" ".join(s1)+" ".join(s2)+s3.upper()
print(result)
     