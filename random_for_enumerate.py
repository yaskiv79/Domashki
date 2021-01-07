import random

random_list = [random.randint(0, 9) for i in range(15)]
print(random_list)
print("Размер списка -", len(random_list), 'чисел')
a = int(input("Введите число от 0 до 9:"))
if a not in random_list:
    print("Число", a, "не найдено в списке")
else:
    for index, element in enumerate(random_list):
        if element == a:
            print("Индекс введенного числа ", element, "-", index)

