def maxchoc(K):
    return ((K // 2) + 1) * ((K - K // 2) + 1)
T = int(input("Enter test cases : ")) 
for _ in range(T):
    K = int(input("no of straight cuts : "))
    print(maxchoc(K))
