def fact(n):
    """  
    It prints factorial of number using recursive approach 
    """
    if n==1:
        return 1
    else:
        return (n*fact(n-1))



print(fact(5))


def fabnoci(n):
    """
    It prints the fabnoci series of the given number using recursive approach
    """
    if n ==1:
        return 0
    elif n==2:
        return 1    
    else:
        return (fabnoci(n-1)+fabnoci(n-2))

print(fabnoci(6))


