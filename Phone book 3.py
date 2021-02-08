import mymodule
print('Меню телефонной книги:')

t = {"Создать", "Найти", "Отредактировать", "Удалить", "Выйти"}
[print(x) for x in t]

def Phone_book():
    a = str(input('Введите пункт меню:',))
    if a == "Выйти":

        mymodule.Exit_program()

    elif a == "Создать":
        print('Этот пункт в разработке')
    elif a == "Найти":
        print('Этот пункт в разработке')
    elif a == "Отредактировать":
        print('Этот пункт в разработке')
    elif a == "Удалить":
        print('Этот пункт в разработке')
    else:
        print('Такого пункта меню не существует. Повторите ввод.')

    Phone_book()
    a = str(input())
Phone_book ()
