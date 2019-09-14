#Pattern Printing 
num=int(input("Enter number -   "))
binary_in=int(input("Enter 0 or 1 -  "))



if (bool(binary_in))==True:
    for i in range(num+1):
        print(i*"*")
else:
    for j in range(num,0,-1):
        print(j*"*")