#pangram or not (mistake)

def pangram(string):
    str.lower()
    L=[] 
    for i in str :
        if i not in ' ':
            L.append(ord(i))
    print(L)
    for i in range(97,123):
        if i in L :
            if i==len(L)-1 :                 
                print("It is a panagram")    
                continue
            else :
                print("Not a panagram")
                break
str=input("Enter string : ")
pangram(str)
#we promptly judged antique ivory buckles for the next prize