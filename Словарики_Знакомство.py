a = ['Фамилия', 'Имя', 'Отчество']
b = input('Введите ФИО:')
b = b.split()

def person(d, r):
    c = {d[0] : r[0], d[1] : r[1], d[2] : r[2]}
    print('Способ первый: ', c)


def person2(w, t):
    t = [[a[0], b[0]], [a[1], b[1]], [a[2], b[2]]]
    r = dict(t)
    print('Способ второй: ', r)

person(a, b)
person2(a, b)