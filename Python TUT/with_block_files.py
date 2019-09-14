#With block automatically close the file 
with open('anjani_1.txt') as f:
    a=f.read(30)
    print(a)

# We can open the file again after with block 

f=open('anjani_1.txt')
print("\n\n\nAgain open the file")
print(f.read())
f.close() 
 