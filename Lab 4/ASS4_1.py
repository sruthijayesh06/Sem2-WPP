#The Love Letter mystery (mistake)

def palindrome(string):
    n=len(string)
    count=0
    #print(string)
    for i in range(n//2):
        left = ord(string[i])
        right = ord(string[n - 1 - i])
        count += abs(left - right)
    print(count)
palindrome(string=input("Enter a string : "))



