#utopian tree

def utopian_tree_growth(n):
    height = 1  
    for cycle in range(1, n + 1): 
        if cycle % 2 == 1:  
            height *= 2
        else: 
            height += 1
    return height
T = int(input("Enter no of test cases : "))  
for i in range(T):
    N = int(input("Enter N : ")) 
    print(utopian_tree_growth(N))
