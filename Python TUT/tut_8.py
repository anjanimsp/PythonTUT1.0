mystr="Anjani is good programmer"
#print(len(mystr))
#print(mystr[0:25])
#print(mystr[0:25:1])
#print(mystr[::])
#Both are same 
#to reverse the string 
#print(mystr[::-1])

#Check whether this string contain alpha numberic strin(Space or not)
print(mystr.isalnum())
#check whether this string ends with ""
print(mystr.endswith('programmer'))
#It prints count of the particular character
print(mystr.count('o'))
#It makes the first charecter of string in capatial letter
print(mystr.capitalize())
#It finds the index of string
print(mystr.find("is"))
#It convert the whole string into lowercase
print(mystr.lower())
#It convert the whole string into uppercase
print(mystr.upper())
#It replaces the string 
print(mystr.replace('is','are'))