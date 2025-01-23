#Consider a 3-D co-ordinate space. Input 10 3-D points. Find the nearest neighbour for each of the points in your 3-D space and
#store them in a list. The final output is a list with each consisting of a point and its nearest neighbour.
#[Hint: Use distance between two points formula]

L=[]
lst=[]
import math
print("Enter 10 3-dimensional coordinates  \n")
for i in range(10) :
    L1=[]
    for j in range(3):
        X=int(input("Enter coordinate : "))
        L1.append(X)
    print("\nEnter",i+2,"set of coordinates : \n")
    L.append(L1)
for i in range(len(L)) :
    for j in range(i+1,len(L)):
        a1,a2,a3=L[i][0],L[i][1],L[i][2]
        b1,b2,b3=L[j][0],L[j][1],L[j][2]
        dist=math.sqrt(((a1-b1)**2)+((a2-b2)**2)+((a3-b3)**2))
        lst.append(dist)
print("\nThe minimum distance is : ",min(lst))
