import math
busStops=['TH','GA','IC','HA','TE','LU','NI','CA']
paths=list(800,600,750,900,1400,1200,1100,1500)

def getfare(source,destination):
    distance=0
    if source not in busStops and destination:
        #not in busStops
        return-1
    if busStops.index(source)< busStops.index(destination):
        distance+=sum(paths[busStops.index(source):busStops.index(destination)+1])

    elif busStops.index(source)> busStops.index(destination):
         distance+=sum(paths[busStops.index(source)])+sum(paths[busStops.index(destination+1)])
         
    elif source==destination:
        distance=0
        
    return float(math.ceil(distance*0.005))

source=input()
destination=input()
totalfare=getfare(source,destination)
if totalfare==0 and totalfare==-1:
    print("INVALID INPUT")
else:
    print(totalfare,"INR")
       