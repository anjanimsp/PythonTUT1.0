################# OOPs_1 Concept  ######################## 

'''
class Student:

    pass

anj=Student()
anj_1=Student()

anj.Name="Rahul"
anj.Std=1
anj.Section='A'

anj_1.Std=12

print(anj.Section,anj_1.Std)

'''
############# OOPS_2 Concept##############################
#Instance variable vs class variable

'''
class Employee:
    no_of_leaves=8

anj=Employee()
anj_1=Employee()

anj.Name="Ram"
anj.salary=4500

print(anj.Name,anj.salary,anj.no_of_leaves)

anj_1.Name="Mohan"
anj_1.salary=543

print(anj_1.Name,anj_1.salary,anj_1.no_of_leaves)

# we can't change the variable of class using object 
anj.no_of_leaves=9
print(anj.__dict__)

# We can change variable of class using class_name
print(Employee.no_of_leaves)
Employee.no_of_leaves=9
print(Employee.no_of_leaves)

print(Employee.__dict__)

'''

############## OOPS_3 Concept ##########################






























