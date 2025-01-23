#Let the user enter products and its prices continuously. store in a dict as key-value pairs. and let user search for it.

n=int(input("Enter number of items to be entered : "))
Dict={}
for i in range(n) :
    item=input("Enter name of product : ").lower()
    price=int(input("Enter price of product (in INR): "))
    Dict[item]=price
while True :
    ch=input("\nEnter item to be searched : ").lower()
    for i in Dict :
        copy=ch
        if ch == i :
            print("\nThe price of",copy,"is : ",Dict[copy])
    print("\n=====================================================\n")
    print("Enter 1 to continue searching","Enter 2 to exit",sep="\n")
    choice=int(input("choice : "))
    if choice != 1:
        break

