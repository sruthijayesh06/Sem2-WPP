#program to find factorial
no=int(input("Enter number : "))
fact=1
for i in range(1,no):
    fact*=i
print("The factorial is : ",fact)
