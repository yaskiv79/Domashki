def high_year(a):
    b = a % 4
    c = a % 100
    d = a % 400
    if b == 0:
        if c == 0:
            if d == 0:
                 print('Год высокосный')
            else:
                print('Год не высокосный')
        else:
            print('Год высокосный')
    else:
        print('Год не высокосный')

year = int(input())
high_year(year)