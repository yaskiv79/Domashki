a = float(input("Введите произвольное число A:"))
b = float(input("Введите еще одно число B:"))
if a == 0 or b == 0:
    print("Числа не должны быть равны нулю")
if a == b:
    print("Числа равны")
if a != 0 and b != 0:
    if a > b:
        res = a - b
        print("A-B=", res)
    elif a < b:
        res = a + b
        print("A+B=", res)
print("Все работает как надо!!!!!")
