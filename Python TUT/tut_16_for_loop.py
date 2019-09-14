#lis=[1,2,4,5,3,2,4,3]
#for i in lis:
#    print(i)
#Nested List

lis_nes=[[1,2],[3,4],[5,6]]
#for i,j in lis_nes:
#    print(i,j)

# for accessing key value pair in dictionary 
dic=dict(lis_nes)
#print(dic)

#for i,j in dic.items():
#    print(i,j)

#Quizz

lis_item=[1,2,"Anjan",'Apple',"air",9,87,65]
for i in lis_item:
    if str(i).isnumeric() and  i>6:
        print(i)
