#iterative method
'''def isvowel(ch):   
  return ch.lower()in ['a','e','i','o','u']
def countvowel(s):
    count=0
    for i in range (len(s)):
        if isvowel(s[i]):
            count+=1
    return count
    

s =input("enter a string:")
print(countvowel(s))'''

  
   #recursive
count=0
def countvowelrecursive(str):
    global count
    #base case
    
    vowel=['a','e','i','o','u']
    if(str[i]==vowel):
        count+=countvowelrecursive(str)
    return count
       
       
str=input("enter the str:")
ans=0
ans=countvowelrecursive(str)
print(ans)