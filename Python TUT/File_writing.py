# writing to a file
#f=open("anjani_1.txt",'a')
#number_of_charatcter=f.write("PHP is a server side script used for website creation")

#Prints the number of character 
#print(number_of_charatcter)

#Open a file in read and write mode both 
f=open('anjani_1.txt','r+')
print(f.read())
f.write("\n thank you")




f.close()