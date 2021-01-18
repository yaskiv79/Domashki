# Создать функцию, которая будет генерировать два списка случайным образом, после чего
# сравнивать элементы этих двух списков и выводить в консоль новый список, который
# будет состоять из элементов, которые есть в обоих оригинальных списках.
def Lists():
    import random

    list1 = [random.randint(1, 20) for i in range(10)]
    list2 = [random.randint(1, 20) for i in range(10)]
    print('list1:', list1)
    print('list2:', list2)
    if list1 < list2:
        print(list1 < list2)
        list3 = list1 + list2
        print(list3)
    list4 = [max(list1)] + [min(list2)]
    print(list4)
Lists()