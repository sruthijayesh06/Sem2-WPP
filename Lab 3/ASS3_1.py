#Q1. digital roots

def digital_root(n):
    while n >= 10:
        add=0
        for digit in str(n): 
            add += int(digit)  
        n = add
    return n

n = int(input("Enter a number: "))
print("The digital root of",n,"is : ", digital_root(n))
