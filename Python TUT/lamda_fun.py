#Lambda Function 

#def add(a,b):
#    return a+b

#add_l=lambda x,y:x+y

#print(add_l(34,5))
#print (add(34,5))

#Retuen the first element of nested list 
def a_first(a):
    return a[1]

#Lambda Function same as the above function
sort_lem=lambda x:x[1]

a=[[1,43],[3,65],[2,30]]

a.sort(key=sort_lem)
print(a)

