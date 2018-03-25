import random

def creatrandmas():
    m = []
    for i in range(10):
        m.append(random.randint(0, 999))
    return m

sortedmasv = creatrandmas()
print (sortedmasv)
sortedmasv = sorted(sortedmasv)
print (sortedmasv)
