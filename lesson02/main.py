import random

#функция, которая создает массив из 10ти случайных чисел
def creatrandmas():
    m = []
    for i in range(10):
        m.append(random.randint(0, 999))
    return m

sortedmasv = creatrandmas()
print (sortedmasv)
#сортировка массива
sortedmasv = sorted(sortedmasv)
print (sortedmasv)

sortedmasv[0],sortedmasv[9] = sortedmasv[9],sortedmasv[0]
print (sortedmasv)

