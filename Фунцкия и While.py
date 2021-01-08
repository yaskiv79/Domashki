def a_function():
    print("\nСравнение закончили")
A = 1
B = 4
print("A=1, B=4")

while A < B:
    print("А пока меньше В")
    A += 1
    res = A + 1
    print("\nA+1=", res)
    if A >= B:
        print("\nА, наконец то, болше В!!!")
a_function()