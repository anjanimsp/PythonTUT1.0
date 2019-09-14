############ map ####################### 

#numbers=["1",'2','3','25']

#for i in range(len(numbers)):
#    numbers[i]=int(numbers[i])

#number_int=list(map(int,numbers))
#print(number_int[2]+10)

#num_square=list(map(lambda x:x*x,number_int))
#print(num_square)

'''
def square(x):
    return x*x

def cube(x):
    return x*x*x

func=[square,cube]

for i in range(5):
    val=list(map(lambda a:a(i),func))
    print(val)
'''

#############  Filter Function #######################

#list_1=[1,2,3,4,5,6,7,8,9,10]

#def greater_5(num):
#    return num>5

#gr_5=list(filter(greater_5,list_1))
#print(gr_5)


######### Reduce Function ###############################

from functools import reduce

lis_1=[1,2,3,4]

'''
sum=0
for i in lis_1:
    sum+=i
print(sum)
'''
#use of Reduce 
num=reduce(lambda x,y:x+y,lis_1)
print(num)








