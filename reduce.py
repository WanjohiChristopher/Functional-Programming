from functools import reduce
#we start with fuction
#remember we are reducing this list
#reduce takes two arguments
ls=[34,54,12,97,78,90,12]

def reduce_func(x,y):
    return x*y

#the we use reduce
out=reduce(reduce_func,ls)
print('This is the output after reducing', out)

#now using lambda functions
outputs=reduce(lambda x,y:x*y,ls)
print('This is the output of the reduce',outputs)