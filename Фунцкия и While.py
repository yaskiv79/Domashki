def Comparing(K):
    B = 8
    while K < B:
        print("K пока меньше В")
        K += 1
        print("\nK + 1 =", K)
        if K >= B:
            print("K, наконец-то, больше В!!!")

for i in range (1, 10):
    Comparing(i)



