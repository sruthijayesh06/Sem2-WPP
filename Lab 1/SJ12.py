#ask user to enter a word and capitalize every alternate word.

str=input("Enter string : ")
for i in range(len(str)) :
        if i%2!=0 :
            print(str[i],end='')
            continue
        else :
            print(str[i].upper(),end='')
            continue
            
