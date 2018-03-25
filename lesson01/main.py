x = input('1е число: ')
y = input('2е число: ')
z = input('3е число: ')
try:
    x = float(x)
except:
    print ('Написано же число, а ты что вводишь?')
    quit()
try:
    y = float(y)
except:
    print ('Написано же число, а ты что вводишь?')
    quit()
try:
    z = float(z)
except:
    print ('Написано же число, а ты что вводишь?')
    quit()
s = x + y + z
print('Сумма 3х чисел: ' + str(s))