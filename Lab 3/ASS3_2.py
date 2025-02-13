#Fibonacci using function (1-1000)

def isfibo(no) :
    L=[0,1]
    sum=0
    for i in range(1,no) :
        sum=L[i]+L[i-1]
        if sum>no :
            break
        L.append(sum)
    print(L)
    return L
n=int(input("Enter no to be checked : "))
L= isfibo(n)
if n in L:  
    print("The number is a part of the Fibonacci series")
else:
    print("The number is NOT a part of the Fibonacci series")