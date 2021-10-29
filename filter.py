#for the filter function it works using this syntax
#answ=filter(function,inputs)
#can either be used as a list or a generator

import pandas as pd
#x=pd.read_csv('diabetes.csv')
x= [0,10,20,30,40,50,60,70,80,90,100]
#x=x[x['Glucose']<10]

def filt_glucose(x):
   filtered=x<42

   return filtered

output=list(filter(filt_glucose,x))
#then we return as a list or a generator
print(output)

#using lambda functions
y=[1,2,3,4,5,6,7,8,9,10]
c_out=filter(lambda y:y<6,y)
print(list(c_out))
    

    