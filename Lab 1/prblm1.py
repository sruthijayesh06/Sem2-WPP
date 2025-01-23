#codedocs admin kidnap problem
#N : no of boxes
#X : box with the coin in it
#S : no of swaps

t = int(input("Enter number of test cases : "))
N=int(input("Enter number of boxes : "))
X=int(input("Enter current position of coin : "))
for j in range(t):
    print("\nTEST CASE", j)
    S=int(input("\nEnter no of swaps : "))
    for i in range(S):
        a=int(input("Enter first box to be swapped : "))
        b=int(input("Enter second box to be swapped : "))
        if X == a:
            X = b
        elif X == b:
            X = a
print("The current position of the coin is : ",X)
