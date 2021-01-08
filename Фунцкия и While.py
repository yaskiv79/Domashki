def a_function():
    print("\nСравнение закончили")


A = 1
B = 4
print("A = 1 B = 4")

while A < B:
    print("А пока меньше В")
    A += 1
    print("\nA + 1 =", A)
    if A >= B:
        print("\nА, наконец-то, больше В!!!")
a_function()
