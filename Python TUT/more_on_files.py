f=open("anjani_1.txt",'r')
#It (tell()) shows the location of file pointer
#print(f.tell())
print(f.readline())
#print(f.tell())

#It seek() reset the file pointer 

f.seek(20)

print(f.readline())
#print(f.tell())



f.close()
