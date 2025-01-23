#Enter names of students not exceeding 15 charecters. Print the reverse of names.

L=[]
n=int(input("Enter no of students : "))
for i in range(n) :
    name=input("Enter name of the student : ")
    L.append(name)
print("\nReversed format of names : ")
for i in L :
    print(i[-1:-16:-1])
