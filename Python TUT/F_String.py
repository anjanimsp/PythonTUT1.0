#F Strings

#me="Anjani"

#str="this is %s"%me
#print(str)

#str = "This is {}"
#b=str.format(me)
#print(b)

#F-String
#str=f"this is {me} {56*2}"
#print(str)

#*args an **kwargs

#def fun_print_name(a,b,c,d):
#    print(a,b,c,d)

#fun_print_name("As","Ak","RJ","Ana")
'''
def fun_args(*args,**kwargs):
    for items in args:
        print(items)
    print("\n")    
    for key,value in kwargs.items():
        print(key,value)    


kw={"A":"Apple","B":"Ball","C":"Cat"}


lis=['AS','Ak',"Aj","RM","New_Item"]
fun_args(*lis,**kw)
'''

#Time module in python 

import time

initial=time.time()



for i in range(145):
    a=i
    #print(i)

print(f"time of running for loop{time.time()-initial} seconds")

initial_2=time.time()

j=0
while (j<145):
    #print(j)
    j+=1
print(f"time of running while loop{time.time()-initial_2} seconds")


local_time=time.asctime(time.localtime(time.time()))
print(local_time)



