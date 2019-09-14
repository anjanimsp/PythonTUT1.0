#Try and Except 
num1=input("Enter num1 -  ")
num2=input("Enter num2-   ")

try:
    print("Sum of two number is ",int(num1)+int(num2))

except Exception as e:
    print(e)

print("This is very important line")    