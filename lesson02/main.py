import random
def creatrandmas():
    m = []
    for i in range(9):
        m.append(random.randint(0, 999))
    return m
masv = creatrandmas()
print (masv)