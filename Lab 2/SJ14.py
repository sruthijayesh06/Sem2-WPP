#You are given a number N, you need to print the number of positions where digits exactly divides N.

test=int(input("Enter number of test cases (>15): "))
L=[]
for i in range(test):
    no=int(input("Enter no to be tested : "))
    L.append(no)
count=0
for i in L :
    count=0
    no=i
    while i>0 :
        d=i%10
        if d==0 :
            count+=1
        elif i%d == 0 :
            count+=1
        i=i//10
    print("The number of positions where digits exactly divides",no,"is : ",count)
