#we will use map function
#map helps in creating a new list by applying a function to each item of a given list
#we stat with function
from time import time
start=time()
def area_circles(a):
    return a*a*3.14
#creates list of radius of circles
radius = [2,5,7.1,0.3,10]
 
 #use map  function now
areas=map(area_circles,radius)

print(list(areas))

print('The time taken for execution is',time()-start)
#lambda function
from time import time
start=time()
outs=list(map(lambda a:a*a*3.14,radius))

print(outs)
print('The time taken for execution is',time()-start)