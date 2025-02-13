S=input("enter any string:")
no_of_stars=0
no_of_hashes=0
for i in S:
    if i== "*" :
        no_of_stars+=1
    else:
        no_of_hashes+=1
print(no_of_stars-no_of_hashes) 