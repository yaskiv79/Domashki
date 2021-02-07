p = {"Создать", "Найти", "Отредактировать", "Удалить", "Выйти"}
print('Введите пункт меню:')
[print(x) for x in p]
a = str(input())
if a == "Выйти":
    import mymodule

    mymodule.Exit_program()
elif a != "Выйти":
    print('Этот пункт в разработке')

