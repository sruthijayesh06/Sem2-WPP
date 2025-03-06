'''
def convert (num) :
    bin=[]
    while num>10 :
        d=num%10
        bin.append(d)
        num=num//10
    bin.reverse()
    return bin
no1=int(input("Enter first number : "))
no2=int(input("Enter second number : "))
bin1,bin2=[],[]
bin1=convert(no1)
bin2=convert(no2)
for i in range(len(bin1)) :
'''
def max_xor(L, R):
    maxval = 0
    for i in range(L, R + 1):
        for j in range(i, R + 1): 
            maxval = max(maxval, i^j)
    return maxval
L = int(input("Enter min : "))
R = int(input("Enter max : "))
print(max_xor(L, R))