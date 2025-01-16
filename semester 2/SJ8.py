#Write a program that asks the user to enter a length in feet. The program should then give the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
#meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they enter a 2, then the program converts to yards,
#etc. While this can be done with if statements,it is much shorter with lists and it is also easier to add new conversions if you use lists.

'''
feet=float(input("Enter length(in feet) : "))
print("\n1.feet into inches","2.feet into yards","3.feet into meters","4.feet into kilometers",sep="\n")
opt=int(input("\nEnter option no : "))
if opt==1 :
    print("\nLength in inches : ",round(feet*12,4))
elif opt==2 :
    print("\nLength in yards : ",round(feet/3,4))
elif opt==3 :
    print("\nLength in meters : ",round(feet/3.281,4))
elif opt==4 :
    print("\nLength in kilometers : ",round(feet/3281,4))
'''

feet=float(input("Enter length(in feet) : "))
L=['inches','yards','meters','kilometers']
conv=[round(feet*12,4),round(feet/3,4),round(feet/3.281,4),round(feet/3281,4)]
print("\n1.feet into inches","2.feet into yards","3.feet into meters","4.feet into kilometers",sep="\n")
opt=int(input("\nEnter option no : "))
print("Length in ",L[opt-1],": ",conv[opt-1])
