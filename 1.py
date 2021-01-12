def Comparing(K, B):
    while K < B:
        print("K пока меньше В")
        K += 1
        print("\nK + 1 =", K)
        if K >= B:
            print("K, наконец-то, больше В!!!")


Comparing(1, 10)
