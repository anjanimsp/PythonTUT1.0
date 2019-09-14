#guess the number which having only 5 trail
num_to_guess=24
no_of_trail=5
while (no_of_trail>0):
    print("number of trail left",no_of_trail)
    num=int(input())
    if  num_to_guess < num:
        print("Please choose less than ",num)
    elif num_to_guess>num:
        print("please choose greater than",num)
    else:
        print("you won")
        print("number of tail",no_of_trail)
        break

    no_of_trail-=1

if no_of_trail==0:
    print("Sorry you loss")            