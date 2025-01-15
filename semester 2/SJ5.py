#program to reverse a given number
no=int(input("Enter number to be reversed : "))
print("The reversed number is :",end=" ")
while no>0 :
    d=no%10
    print(d,end="")
    no=no//10
    
