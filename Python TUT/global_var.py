# Global Variables 

x=100
def fun_glob():
    x=90
    def var_glob():
        global x 
        x=99

    print("Before calling var_glob function",x)
    var_glob()
    print("After calling var_glob function",x)


fun_glob()
print(x)