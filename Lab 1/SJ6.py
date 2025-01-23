#Create the following lists using a for loop.
#(a) A list consisting of the integers 0 through 49
#(b) A list containing the squares of the integers 1 through 50.
#(c) The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z.

import math
def printno() :
    L=[]
    for i in range(50) :
        L.append(i)
    print("a) ",L)
def square() :
    L=[]
    for i in range(51) :
        L.append(pow(i,2))
    print("b) ",L)
def letter() :
    L=[]
    str=''
    for i in range(1,27):
        L.append(chr(96+i)*i)
    print("c) ",L)  
printno()
print("\n")
square()
print("\n")
letter()
