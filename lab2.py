a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if a < b and a < c:
    d = a
elif b < c and b < a:
    d = b
elif c < b and c < a:
    d = c

print(' ')
print('Наименьшее число: ', d)